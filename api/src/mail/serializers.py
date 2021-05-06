from rest_framework import serializers
from rest_framework.exceptions import ValidationError


class EmailSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255, required=True)
    email = serializers.EmailField(required=True)
    phone = serializers.CharField(max_length=11, required=True)
    message = serializers.CharField(max_length=1000, required=True)

    def validate(self, attrs):
        phone = attrs['phone']

        if (phone.startswith('79') is False) or (len(phone) != 11) or (phone.isnumeric() is False):
            raise ValidationError({'phone': 'Invalid phone number'})

        return attrs
