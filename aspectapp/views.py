# aspectapp/views.py

# openai 라이브러리와 decouple 라이브러리를 임포트합니다.
import openai
from decouple import config
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class CompareProductsView(APIView):
    def post(self, request):
        products = request.data.get("products")

        comparisons = generate_comparison(products)

        return Response({"비교 결과": comparisons})

def generate_comparison(products):
    openai.api_key = config('OPENAI_API_KEY')

    if len(products) < 2 or len(products) > 5:
        return []

    aspect_lists = []
    for idx, product in enumerate(products, start=1):
        prompt = f"비교 기준 {idx}:\n\n{products[idx - 1]}\n"
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=500
        )
        aspect_lists.append(response.choices[0].text.strip())

    return aspect_lists
