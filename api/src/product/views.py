from django.shortcuts import render
from rest_framework import viewsets, filters, status, mixins, generics
from product import serializers
from product import models
# from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated


class CategoryViewSet(viewsets.ModelViewSet):
    """CRUD category"""
    # authentication_classes = (JWTAuthentication,)
    # permission_classes = (IsAuthenticated,)
    serializer_class = serializers.CategorySerializer
    queryset = models.Category.objects.all()


class SubcategoryViewSet(viewsets.ModelViewSet):
    """CRUD subcategory"""
    # authentication_classes = (JWTAuthentication,)
    # permission_classes = (IsAuthenticated,)
    serializer_class = serializers.SubcategorySerializer
    queryset = models.Subcategory.objects.all()


class BrandViewSet(viewsets.ModelViewSet):
    """CRUD brand"""
    # authentication_classes = (JWTAuthentication,)
    # permission_classes = (IsAuthenticated,)
    serializer_class = serializers.BrandSerializer
    queryset = models.Brand.objects.all()


class CityViewSet(viewsets.ModelViewSet):
    """CRUD city"""
    # authentication_classes = (JWTAuthentication,)
    # permission_classes = (IsAuthenticated,)
    serializer_class = serializers.CitySerializer
    queryset = models.City.objects.all()


class DaysViewSet(viewsets.ModelViewSet):
    """CRUD days"""
    # authentication_classes = (JWTAuthentication,)
    # permission_classes = (IsAuthenticated,)
    serializer_class = serializers.DaysSerializer
    queryset = models.Days.objects.all()


class DiscountViewSet(viewsets.ModelViewSet):
    """CRUD discount"""
    # authentication_classes = (JWTAuthentication,)
    # permission_classes = (IsAuthenticated,)
    serializer_class = serializers.DiscountSerializer
    queryset = models.Discount.objects.all()


class ItemDiscountViewSet(viewsets.ModelViewSet):
    """CRUD itemdiscount"""
    # authentication_classes = (JWTAuthentication,)
    # permission_classes = (IsAuthenticated,)
    serializer_class = serializers.ItemDiscountSerializer
    queryset = models.ItemDiscount.objects.all()


class ProductViewSet(viewsets.ModelViewSet):
    """CRUD product"""
    # authentication_classes = (JWTAuthentication,)
    # permission_classes = (IsAuthenticated,)
    serializer_class = serializers.ProductSerializer
    queryset = models.Product.objects.all()
    filter_backends = [filters.SearchFilter]
    filterset_fields = ['category', 'subcategory', 'brand', 'city']
    search_fields = ['price', 'title']

