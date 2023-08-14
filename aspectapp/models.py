# aspectapp/models.py

from django.db import models


# Product 모델 클래스를 정의합니다. models.Model을 상속받습니다.
class Product(models.Model):
    # productName 필드를 정의합니다. 최대 길이 200으로 설정됩니다.
    productName = models.CharField(max_length=200)

    # productReview 필드를 정의합니다. 긴 텍스트를 저장하기 위한 필드입니다.
    productReview = models.TextField()

    # mallProductUrl 필드를 정의합니다. 긴 텍스트를 저장하기 위한 필드입니다.
    mallProductUrl = models.TextField()

    # 객체의 문자열 표현을 정의합니다. 객체가 문자열로 표시될 때 productName을 반환합니다.
    def __str__(self):
        return self.productName
