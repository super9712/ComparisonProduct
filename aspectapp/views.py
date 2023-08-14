# aspectapp/views.py

# aspectapp/views.py

# openai 라이브러리와 decouple 라이브러리를 임포트합니다.
import openai
from decouple import config
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# AspectProductsView 클래스를 정의합니다. APIView를 상속받습니다.
class AspectProductsView(APIView):
    # HTTP GET 요청에 대한 처리를 위한 메서드입니다.
    def get(self, request):
        # GET 요청의 쿼리 파라미터에서 'product' 값을 리스트로 가져옵니다.
        products = request.query_params.getlist("product")

        # 제품의 수가 2개 미만일 경우 오류 응답을 반환합니다.
        if len(products) < 2:
            return Response({"에러": "적어도 두 가지 제품을 기입하세요."}, status=status.HTTP_400_BAD_REQUEST)

        # generate_comparison_questions 메서드를 호출하여 비교 결과를 생성합니다.
        aspect_list = self.generate_comparison_questions(products[0], products[1])

        # 생성된 비교 결과를 응답합니다.
        return Response({"비교 결과": aspect_list})

    # 제품 비교 기준을 생성하는 메서드입니다.
    def generate_comparison_questions(self, product1, product2):
        # OpenAI API 키를 설정합니다. 환경 변수에서 가져옵니다.
        openai.api_key = config('OPENAI_API_KEY')

        # 입력 프롬프트를 생성합니다.
        prompt = f"{product1}과 {product2}의 비교기준을 6가지로 나타내세요."

        # OpenAI API를 호출하여 모델의 응답을 생성합니다.
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=500
        )

        # 생성된 응답에서 비교 결과를 추출합니다.
        aspect_list = response.choices[0].text.strip()

        # 비교 결과를 쉼표로 분리하여 리스트로 변환합니다.
        aspect_names = aspect_list.split(', ')

        # 비교 결과에 번호를 매겨 리스트로 변환합니다.
        numbered_aspects = [f"{idx + 1}. {aspect}" for idx, aspect in enumerate(aspect_names)]

        # 번호가 매겨진 비교 결과를 반환합니다.
        return numbered_aspects
