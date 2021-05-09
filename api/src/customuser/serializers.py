from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.contrib.auth import password_validation
from customuser.models import Client, UserMode
from subscription.serializers import SubscriptionSerializer


class PasswordChangeSerializer(serializers.ModelSerializer):
    old_password = serializers.CharField(max_length=255, required=True)
    new_password = serializers.CharField(max_length=255, required=True)
    repeat_password = serializers.CharField(max_length=255, required=True)

    class Meta:
        model = Client
        fields = ['old_password', 'new_password', 'repeat_password']

    def get_user(self):
        return Client.objects.get(id=self.context['request'].user.id)

    def validate(self, attrs):
        user = self.get_user()
        password_validation.validate_password(attrs['old_password'], user.password)
        if not attrs['new_password'] == attrs['repeat_passsword']:
            raise ValidationError({'new_password': 'Passwords are not equal'})
        return attrs
    
    def update(self, instance, validated_data): 
        instance.set_password(validated_data['new_password'])
        instance.save()
        return instance


class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        exclude = ['password']


class ProfileSerializer(serializers.ModelSerializer):
    is_subscribed = serializers.ReadOnlyField(source='subscription.is_subscribed')
    client = ClientSerializer(read_only=True)

    class Meta:
        model = UserMode
        fields = '__all__'
