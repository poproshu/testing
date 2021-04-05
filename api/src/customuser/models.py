from django.db import models
from django.contrib.auth.models import User


class City(models.Model):
    city = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.city


class Address(models.Model):
    street = models.CharField(max_length=255)
    house = models.CharField(max_length=255)
    flat_number = models.CharField(max_length=255, blank=True)
    flor = models.IntegerField(blank=True)
    entrance_number = models.CharField(max_length= 255, blank=True)
    intercome_code = models.CharField(max_length=255, blank=True)  

    def __str__(self):
        return f'{self.street}, {self.house}'


class CustomUser(models.Model):
    default_user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.ManyToManyField(Address, blank=True, related_name='user')
    phone = models.IntegerField(blank=True, null=True, unique=True)
    avatar = models.ImageField(upload_to='images/avatar/', blank=True, null=True)
    # favorite = 
    birth_date = models.DateField(blank=True)
    user_city = models.ForeignKey(City, blank=True, null=True, on_delete=models.SET_NULL)
    is_subscribed = models.BooleanField(default=False)
    email_notification = models.BooleanField(default=False)
    tg_notification = models.BooleanField(default=False)
    phone_notification = models.BooleanField(default=False)
    ws_notification = models.BooleanField(default=False)
    # passport 

    def __str__(self):
        return self.default_user.email