from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework import mixins, generics, viewsets
from rest_framework.exceptions import ValidationError
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from customuser.models import Client, UserMode
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
        mode = self.request.query_params.get('mode', None)
        if not mode:
            raise ValidationError({'mode': 'Missing query param'})
        return get_object_or_404(UserMode, client__id=self.request.user.id, mode=mode)
# Create your views here.
