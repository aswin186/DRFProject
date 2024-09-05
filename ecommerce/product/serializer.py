from rest_framework import serializers

from .models import Brand, Product, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['name']


class ProductSerializer(serializers.ModelSerializer):

    brand = BrandSerializer()
    Category = CategorySerializer()

    class Meta:
        model = Product
        fields = '__all__'



# py manage.py startapp product ./drfecommerce/product