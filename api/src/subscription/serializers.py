from rest_framework import serializers
from subscription.models import Subscription
from customuser.models import UserMode


class SubscriptionSerializer(serializers.ModelSerializer):
    is_subscribed = serializers.ReadOnlyField()

    class Meta:
        model = Subscription
        fields = '__all__'
        read_only_field = ['user', 'expires_at', 'is_subscribed']       
    
    def create(self, validated_data):
        user = UserMode.objects.get(client__id=self.context['request'].user.id, mode=1)
        sub = Subscription.objects.create(
            user=user,
            period=validated_data['period'])
        return sub