from rest_framework import serializers
from product import models


class CategorySerializer(serializers.ModelSerializer):
    """Category serializer"""

    class Meta:
        model = models.Category
        fields = '__all__'


class SubcategorySerializer(serializers.ModelSerializer):
    """Subcategory serializer"""

    class Meta:
        model = models.Subcategory
        fields = '__all__'


class BrandSerializer(serializers.ModelSerializer):
    """Brand serializer"""

    class Meta:
        model = models.Brand
        fields = '__all__'


class CitySerializer(serializers.ModelSerializer):
    """City serializer"""

    class Meta:
        model = models.City
        fields = '__all__'


class DaysSerializer(serializers.ModelSerializer):
    """Days serializer"""

    class Meta:
        model = models.Days
        fields = '__all__'


class DiscountSerializer(serializers.ModelSerializer):
    """Discount serializer"""

    class Meta:
        model = models.Discount
        fields = '__all__'


class ItemDiscountSerializer(serializers.ModelSerializer):
    """ItemDiscount serializer"""

    class Meta:
        model = models.ItemDiscount
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    """Product serializer"""

    class Meta:
        model = models.Product
        fields = '__all__'