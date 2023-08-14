# aspectapp/serializers.py

from rest_framework import serializers

# ProductSerializer 클래스를 정의합니다. serializers.Serializer를 상속받습니다.
class ProductSerializer(serializers.Serializer):
    # productName 필드를 정의합니다. 최대 길이 100으로 설정됩니다.
    productName = serializers.CharField(max_length=100)

    # productReview 필드를 정의합니다. (기본 설정은 필요한 파라미터가 없습니다.)
    productReview = serializers.CharField()

    # mallProductUrl 필드를 정의합니다. URL 형식의 필드입니다.
    mallProductUrl = serializers.URLField()
