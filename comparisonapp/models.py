from django.db import models

class ComparisonResult(models.Model):
    products = models.JSONField()  # JSON 형태로 상품 정보 저장
    recommendation = models.TextField()  # 추천 결과 설명

    def __str__(self):
        return f"Comparison Result #{self.pk}"
