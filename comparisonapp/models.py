from django.db import models
from aspectapp.models import Product

# ComparisonResult 모델 클래스를 정의합니다. models.Model을 상속받습니다.
class ComparisonResult(models.Model):
    # product1 필드를 정의합니다. Product 모델과의 외래키 관계를 나타냅니다.
    # 해당 제품이 삭제될 경우 관련된 비교 결과도 함께 삭제됩니다.
    # Product 모델과의 관계를 related_name을 통해 역참조 가능하게 설정합니다.
    product1 = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comparisons_as_product1')

    # product2 필드를 정의합니다. Product 모델과의 외래키 관계를 나타냅니다.
    # 해당 제품이 삭제될 경우 관련된 비교 결과도 함께 삭제됩니다.
    # Product 모델과의 관계를 related_name을 통해 역참조 가능하게 설정합니다.
    product2 = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comparisons_as_product2')

    # aspect 필드를 정의합니다. 비교하는 측면을 나타내는 문자열 필드입니다.
    aspect = models.CharField(max_length=20)

    # recommendation 필드를 정의합니다. 추천 내용을 저장하기 위한 긴 텍스트 필드입니다.
    recommendation = models.TextField()

    # 객체의 문자열 표현을 정의합니다. 비교 결과의 요약을 반환합니다.
    def __str__(self):
        return f"{self.product1} vs {self.product2} - {self.aspect}"
