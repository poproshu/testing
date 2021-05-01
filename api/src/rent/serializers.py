from rest_framework import serializers
from django.shortcuts import get_object_or_404
from rent.models import Rent
from customuser.models import Client, UserMode
from product.models import Product


class CreateRentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rent
        fields = '__all__'
        read_only_fields = ['status', 'owner', 'receiver', 'contract', 'created_at']
    
    def validate(self, attrs):
        return attrs
    
    def get_user(self):
        return self.context.get('request', None).user
    
    def get_client(self):
        user = self.get_user()
        return get_object_or_404(Client, id=user.id)
    
    def get_receiver(self):
        client = self.get_cliend()
        return get_object_or_404(UserMode, customuser=client, mode='Give')

    def create(self, validated_data):
        receiver = self.get_receiver()
        owner = validated_data['product'].user
        rent = Rent.objects.create(
            product=validated_data['product'],
            owner=owner,
            receiver=receiver,
            # payment_method=validated_data['payment_method'],
            start_date=validated_data['start_date'],
            end_date=validated_data['end_date']
        )
        return rent

