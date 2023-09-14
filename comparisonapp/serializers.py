# comparisonapp/serializers.py

from rest_framework import serializers
from .models import ComparisonResult

class CompareProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComparisonResult
        fields = '__all__'
