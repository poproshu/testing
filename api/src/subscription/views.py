from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from subscription.models import Subscription
from subscription.serializers import SubscriptionSerializer


class SubscriptionViewSet(viewsets.ModelViewSet):
    serializer_class = SubscriptionSerializer
    permission_classes = [IsAuthenticated,]
    authentication_classes = (JWTAuthentication,)
    queryset = Subscription.objects.all()

# Create your views here.
