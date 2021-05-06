from rest_framework import serializers
from product import models
from customuser.models import UserMode


class FavoriteSerializer(serializers.ModelSerializer):
    """Favorites serializer"""
    class Meta:
        model = models.Favorite
        fields = '__all__'
        read_only_fields = ['user']
    
    def create(self, validated_data):
        user = UserMode.objects.get(client__id=self.context['request'].user.id, mode=0)
        favorite = models.Favorite.objects.create(
            product=validated_data['product'],
            user=user
        )
        return favorite



class DeliverySerializer(serializers.ModelSerializer):
    """Delivery serializer"""

    class Meta:
        model = models.Discount
        fields = '__all__'


class ProductImageSerializer(serializers.ModelSerializer):
    """ProductImage serializer"""
    
    class Meta:
        model = models.ProductImage
        fields = '__all__'
        read_only_fields = ['owner']
    
    def create(self, validated_data):
        user = UserMode.objects.get(client__id=self.context['request'].user.id, mode=1)
        product_image = models.ProductImage.objects.create(
            image=validated_data['image'],
            owner=user
        )
        return product_image
        

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