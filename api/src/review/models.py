from django.db import models
from product.models import Product
from customuser.models import UserMode


class Review(models.Model):
    """*** Отзывы ***"""
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="product")
    owner = models.ForeignKey(
        UserMode,
        on_delete=models.CASCADE,
        related_name="Comment_reciever",
        limit_choices_to={'mode': '0'})
    body = models.TextField(max_length=1100)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Сортируем по дефолту по дате публикации 
        ordering = ['date',]

    def __str__(self):
        return str(self.owner)


class Comment(models.Model):
    """*** Комментарии ***"""
    owner = models.ForeignKey(
        UserMode,
        on_delete=models.CASCADE,
        limit_choices_to={'mode': '1'},
        related_name="comment_owner")
    reciever = models.ForeignKey(
        UserMode,
        on_delete=models.CASCADE,
        limit_choices_to={'mode': '0'},
        related_name="comment_reciever")
    body = models.TextField(max_length=1100)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date',]

    def __str__(self):
        return f'Owner: {self.owner}; date" {self.date}'