# comparisonapp/views.py

import openai
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from decouple import config

class CompareProductsView(APIView):
    def post(self, request):
        selected_aspect = request.data.get("aspects")
        products = request.data.get("products")

        if not selected_aspect or len(products) < 2 or len(products) > 10:
            return Response({"error": "적절한 요청 데이터를 제공하세요."}, status=status.HTTP_400_BAD_REQUEST)

        recommendations = self.generate_recommendations(products, selected_aspect)

        return Response({"추천 결과": recommendations})

    def generate_recommendations(self, products, selected_aspect):
        openai.api_key = config('OPENAI_API_KEY')

        recommendations = []

        for product in products:
            query = f"{selected_aspect} 측면에서 {product} 중 더 좋은 제품을 골라줘."
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": query}
                ]
            )

            recommendation = response.choices[0].message.content.strip()

            recommendations.append({
                "product": product,
                "aspect": selected_aspect,
                "recommendation": recommendation
            })

        return recommendations
