from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import GenericAPIView, CreateAPIView
from customuser.models import Client
from authclient.serializers import RegistrationSerializer, LoginSerializer


# VIEW - АВТОРИЗАЦИЯ ПОЛЬЗОВАТЕЛЯ
class LoginAPIView(GenericAPIView):
    serializer_class = LoginSerializer
    
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(data=serializer.validated_data, status=status.HTTP_200_OK)
# /////////////////////////////////        

    
# VIEW - РЕГИСТРАЦИЯ НОВОГО ПОЛЬЗОВАТЕЛЯ
class RegisterAPIView(CreateAPIView):
    serializer_class = RegistrationSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)