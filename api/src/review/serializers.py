from rest_framework import serializers
from review.models import Review, Comment
from customuser.models import Client, UserMode


class ReviewsSerializer(serializers.ModelSerializer):
    """*** ОТЗЫВЫ ***"""
    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ['owner',]
    
    def validate(self, attrs):
        reciever = attrs['product'].owner.client
        sender = self.context['request'].user
        if sender == reciever: 
            raise serializers.ValidationError({"review_error": "Something went wrong. You can not send reviews to your self"})
        return attrs

    def create(self, validated_data):
        review = Review.objects.create(
            product=validated_data['product'],
            owner=UserMode.objects.get(client=self.context['request'].user, mode=0),
            body=validated_data['body'])
        return review


class CommentsSerializer(serializers.ModelSerializer):
    """*** Комментарии ***"""
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ['owner',]

    def validate(self, attrs):
        reciever = attrs['reciever'].client
        sender = self.context['request'].user 
        if sender == reciever: 
            raise serializers.ValidationError({"comment_error": "Something went wrong. You can not send comments to your self"})
        return attrs
    
    def create(self, validated_data):
        comment = Comment.objects.create(
            owner = UserMode.objects.get(id=self.context['request'].user.id, mode=1),
            reciever = UserMode.objects.get(id=validated_data['reciever'].id, mode=0),
            body = validated_data['body'])
        return comment