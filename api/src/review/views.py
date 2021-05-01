from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from review.serializers import ReviewsSerializer, CommentsSerializer
from review.models import Review, Comment


class ReviewsView(viewsets.ModelViewSet):
    """*** Отзывы ***"""
    serializer_class = ReviewsSerializer
    permission_classes = [IsAuthenticated,]
    queryset = Review.objects.all()


class CommentsView(viewsets.ModelViewSet):
    """*** Комментарии ***"""
    serializer_class = CommentsSerializer
    permission_classes = [IsAuthenticated,]
    queryset = Comment.objects.all()