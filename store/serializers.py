from rest_framework import serializers
from .models import Category, Product, Order

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model  = Category
        fields = ['id', 'name', 'description']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Product
        fields = ['id', 'name', 'description', 'price', 'stock', 'category']

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Order
        fields = ['id', 'product', 'quantity', 'status', 'created_at']
