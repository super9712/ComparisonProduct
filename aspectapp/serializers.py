# aspectapp/serializers.py

from rest_framework import serializers

class ProductSerializer(serializers.Serializer):
    object_name = serializers.CharField()
    img_text = serializers.CharField()
    comments = serializers.CharField()
