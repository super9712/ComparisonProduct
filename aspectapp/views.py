# aspectapp/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import openai
from decouple import config

class CompareProductsView(APIView):
    def get(self, request):
        products = request.query_params.getlist("product")

        if len(products) < 2:
            return Response({"에러": "적어도 두 가지 제품을 기입하세요."}, status=status.HTTP_400_BAD_REQUEST)

        aspect_list = self.generate_comparison_questions(products[0], products[1])
        return Response({"비교 결과": aspect_list})

    def generate_comparison_questions(self, product1, product2):
        openai.api_key = config('OPENAI_API_KEY')

        aspects = ["quality", "price", "design", "performance", "reviews", "features"]
        questions = []

        for aspect in aspects:
            prompt = f"{aspect}측면에서 {product1}과 {product2} 중 어느 제품이 더 좋은 제품인가요?"
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=prompt,
                max_tokens=500
            )
            answer = response.choices[0].text.strip()
            questions.append(answer)

        return questions