from rest_framework import serializers
from .models import Product

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'image_url', 'price', 'stock')
        