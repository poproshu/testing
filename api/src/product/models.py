from django.db import models
from django.conf import settings
from staffuser.models import StaffUser

# Create your models here.

class Category(models.Model):
    """Product categories"""
    name = models.CharField(max_length=255, unique=True)
    image = models.ImageField(null=True, blank=True, upload_to='images/categories')

    class Meta:
        verbose_name_plural = "Categories"


    def __str__(self):
        return self.name


class Subcategory(models.Model):
    """Subcategories"""
    name = models.CharField(max_length=255, unique=True)
    image = models.ImageField(null=True, blank=True, upload_to='images/subcategories')
    category = models.ForeignKey(Category, null=True, on_delete=models.CASCADE, related_name='subcategories')

    class Meta:
        verbose_name_plural = "Subcategories"


    def __str__(self):
        return self.name


class Brand(models.Model):
    """Brand"""
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class City(models.Model):
    """City"""
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Option(models.Model):
    """Different price options depends on rent time"""
    
    class TimeChoices(models.TextChoices):
        day = '1 day'
        week = '1 week'
        month = '1 month'

    time = models.CharField(choices=TimeChoices.choices, blank=True, max_length=255, verbose_name='rent time')
    price = models.IntegerField(null=True, blank=True)


class Days(models.Model):
    """Days"""

    class PeriodChoices(models.TextChoices):
        day_1 = '1 day'
        day_2 = '2 days'
        day_3 = '3 days'
        day_4 = '4 days'
        day_5 = '5 days'
        day_6 = '6 days'
        week_1 = '1 week'
        week_2 = '2 weeks'
        week_3 = '3 weeks'
        month = '1 month'
    
    period = models.CharField(choices=PeriodChoices.choices, max_length=255, verbose_name='rent period')

    def __str__(self):
        return self.period

class Discount(models.Model):
    """Discount"""

    class DiscountChoices(models.IntegerChoices):
        discount_1 = 10
        discount_2 = 20
        discount_3 = 30
        discount_4 = 40
        discount_5 = 50
        discount_6 = 60
        discount_7 = 70
        discount_8 = 80
        discount_9 = 90
        discount_10 = 100
    
    discount = models.IntegerField(choices=DiscountChoices.choices, verbose_name='discount')

    def __str__(self):
        return str(self.discount)


class ItemDiscount(models.Model):
    """Item Discount"""
    days = models.ForeignKey(Days, on_delete=models.CASCADE, related_name='item_discount')
    dicounts = models.ForeignKey(Discount, on_delete=models.CASCADE, related_name='item_discount')

    def __str__(self):
        return f'{self.days}: {self.dicounts}'


class Product(models.Model):
    """Products"""
    user = models.ForeignKey(StaffUser, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=255)
    image = models.ImageField(null=True, blank=True, upload_to='images/products')
    description = models.TextField(blank=True)
    price = models.IntegerField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='products')
    subcategory = models.ForeignKey(Subcategory, on_delete=models.SET_NULL, null=True, related_name='products')
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, related_name='products')
    discount = models.ManyToManyField(ItemDiscount, related_name='products')
    condition = models.IntegerChoices('condition', '1 2 3 4 5 6 7 8 9 10')
    purchase_price = models.IntegerField(blank=True, null=True)
    pledge = models.IntegerField(blank=True, null=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, related_name='products')
    inside_city = models.IntegerField(blank=True, null=True, verbose_name='price within the city')
    outside_city = models.IntegerField(blank=True, null=True, verbose_name='price within the city')
    delivery = models.IntegerField(blank=True, null=True, verbose_name='delivery price')
    pickup = models.CharField(max_length=800, blank=True, verbose_name='pickup address')

    def __str__(self):
        return self.title




