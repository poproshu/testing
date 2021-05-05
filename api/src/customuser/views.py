from django.shortcuts import render
from rest_framework import mixins, generics, viewsets
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from customuser.models import Client
from customuser.serializers import PasswordChangeSerializer, ProfileSerializer


class PasswordChangeView(generics.UpdateAPIView):
    serializer_class = PasswordChangeSerializer
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return Client.objects.get(id=self.request.user.id)


class ProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return Client.objects.get(id=self.request.user.id)
# Create your views here.
