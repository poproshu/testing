from re import S
from django.shortcuts import render
from rest_framework import request, viewsets, filters, status, mixins, generics, views
from product import serializers
from product import models
from customuser.models import UserMode
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class ProductPromoteServicePriceAPIView(views.APIView):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        object = models.ProductPromoteServicePrice.objects.last()
        serializer = serializers.ProductPromeServicePriceSerializer(instance=object)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProductPromoteContractViewSet(viewsets.ModelViewSet):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.ProductPromoteContractSerialzier

    def get_queryset(self):
        if self.request.user.is_staff:
            return models.ProductPromoteContract.objects.all()
        return models.ProductPromoteContract.objects.filter(product__user__client__id=self.request.user.id)


class FavoriteViewSet(viewsets.ModelViewSet):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.FavoriteSerializer
    
    def get_queryset(self):
        return models.Favorite.objects.filter(user__client__id=self.request.user.id)


class DeliveryViewSet(viewsets.ModelViewSet):
    # authentication_classes = (JWTAuthentication,)
    # permission_classes = (IsAuthenticated,)
    serializer_class = serializers.ProductImageSerializer
    queryset = models.Delivery.objects.all()


class ProductImageViewSet(viewsets.ModelViewSet):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.ProductImageSerializer

    def get_queryset(self):
        user = UserMode.objects.get(client=self.request.user.id, mode=1)
        return models.ProductImage.objects.filter(owner=user)


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
    filterset_fields = ['category']



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

