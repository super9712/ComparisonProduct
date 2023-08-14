import openai
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from decouple import config


# CompareProductsView 클래스를 정의합니다. APIView를 상속받습니다.
class CompareProductsView(APIView):
    # HTTP GET 요청에 대한 처리를 위한 메서드입니다.
    def get(self, request):
        # GET 요청의 쿼리 파라미터에서 선택된 측면, 제품1, 제품2을 가져옵니다.
        selected_aspect = request.query_params.get("selected_aspect")
        product1 = request.query_params.get("product1")
        product2 = request.query_params.get("product2")

        # 필수 데이터가 누락되었을 경우 오류 응답을 반환합니다.
        if not selected_aspect or not product1 or not product2:
            return Response({"에러": "적절한 요청 데이터를 제공하세요."}, status=status.HTTP_400_BAD_REQUEST)

        # generate_recommendation 메서드를 호출하여 추천 결과를 생성합니다.
        recommendation = self.generate_recommendation(product1, product2, selected_aspect)

        # 생성된 추천 결과를 응답합니다.
        return Response({"추천 결과": recommendation})

    # 제품 추천을 생성하는 메서드입니다.
    def generate_recommendation(self, product1, product2, selected_aspect):
        # OpenAI API 키를 설정합니다. 환경 변수에서 가져옵니다.
        openai.api_key = config('OPENAI_API_KEY')

        # 입력 프롬프트를 생성합니다.
        prompt = f"{selected_aspect} 측면에서 {product1}과 {product2}을 비교한 후 더 좋은 제품을 추천해주세요."

        # OpenAI API를 호출하여 모델의 응답을 생성합니다.
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=500
        )

        # 생성된 응답에서 추천 결과를 추출합니다.
        recommendation = response.choices[0].text.strip()

        # 추천 결과를 반환합니다.
        return recommendation
