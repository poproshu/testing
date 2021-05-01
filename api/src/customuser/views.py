from django.shortcuts import render
from rest_framework import mixins, generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from customuser.models import Client
from customuser.serializers import PasswordChangeSerializer


class PasswordChangeView(generics.UpdateAPIView):
    serializer_class = PasswordChangeSerializer
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        # May raise a permission denied
        self.check_object_permissions(self.request, obj)
        return Client.objects.get(id=self.request.user.id)

# Create your views here.
