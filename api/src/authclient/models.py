from django.db import models
from customuser.models import Client


class EmailCode(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    code = models.CharField(max_length=12)

    def __str__(self):
        return f'{self.client.username}: {self.code}'