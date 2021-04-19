from rest_framework import serializers, exceptions
from django.db.models import Q
from django.contrib.auth import password_validation
from rest_framework_simplejwt.tokens import RefreshToken

from customuser.models import Client


class LoginSerializer(serializers.Serializer):
    email_or_username = serializers.CharField(max_length=255, required=True)
    password = serializers.CharField(max_length=65, min_length=6, required=True)

    def get_token(self, user):
        refresh = RefreshToken.for_user(user)
        return refresh

    def validate(self, attrs):
        user = Client.objects.filter(Q( username=attrs['email_or_username'] ) | Q( email=attrs['email_or_username'] )).first()
        if not user or not user.check_password(attrs['password']):
            raise serializers.ValidationError({"LoginError": "Please make sure you provide correct values"})

        refresh = self.get_token(user)
        access = refresh.access_token
        return { 'access': str(access), 'refresh': str(refresh) }

    
# SERIALIZER -  СЕРИАЛАЙЗЕР РЕГИСТРАЦИИ НОВОГО ПОЛЬЗОВАТЕЛЯ
class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True, required=True,)

    class Meta:
        model = Client
        fields = ['id', 'username', 'email', 'password', 'password2']
        extra_kwargs = {
            'password': {
               'write_only': True
            }
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"passwordError": "Password fields didn't match."})
        return attrs
    
    def validate_password(self, value):
        password_validation.validate_password(value, self.instance)
        return value
    
    def create(self, validated_data):
        user = Client.objects.create(
            username=validated_data['username'],
            email=validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()

        return user