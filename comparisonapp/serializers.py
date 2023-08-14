# comparisonapp/serializers.py

from rest_framework import serializers

# CompareProductsSerializer 클래스를 정의합니다. serializers.Serializer를 상속받습니다.
class CompareProductsSerializer(serializers.Serializer):
    # product1 필드를 정의합니다. 문자열을 저장하기 위한 필드입니다.
    product1 = serializers.CharField()

    # product2 필드를 정의합니다. 문자열을 저장하기 위한 필드입니다.
    product2 = serializers.CharField()

    # recommendation 필드를 정의합니다. 문자열을 저장하기 위한 필드입니다.
    recommendation = serializers.CharField()
