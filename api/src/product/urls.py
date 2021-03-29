from django.urls import path, include
from rest_framework.routers import DefaultRouter
from product import views


router = DefaultRouter()
router.register('products', views.ProductViewSet)
router.register('categories', views.CategoryViewSet)
router.register('subcategories', views.SubcategoryViewSet)
router.register('brands', views.BrandViewSet)
router.register('cities', views.CityViewSet)
router.register('days', views.DaysViewSet)
router.register('discounts', views.DiscountViewSet)
router.register('itemsdicount', views.ItemDiscountViewSet)


urlpatterns = [
    path('', include(router.urls)),
]