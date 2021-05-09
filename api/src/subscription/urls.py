from django.urls import path, include
from rest_framework.routers import DefaultRouter
from subscription import views


router = DefaultRouter()
router.register('subscriptions', views.SubscriptionViewSet)


urlpatterns = [
    path('', include(router.urls)),
]