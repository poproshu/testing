from django.db import models
from django.conf import settings
from datetime import timedelta
from django.utils.timezone import now
from django.core.exceptions import ValidationError
from django.db.models.fields.related import ForeignKey
from customuser.models import UserMode

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
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories')

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


# class Option(models.Model):
#     """Different price options depends on rent time"""
    
#     class TimeChoices(models.TextChoices):
#         day = '1 day'
#         week = '1 week'
#         month = '1 month'

#     time = models.CharField(choices=TimeChoices.choices, blank=True, max_length=255, verbose_name='rent time')
#     price = models.IntegerField(null=True, blank=True)


class Days(models.Model):
    """Days"""
    period = models.CharField(max_length=255, verbose_name='rent period')

    def __str__(self):
        return self.period


class Discount(models.Model):
    """Discount"""
    discount = models.PositiveIntegerField(verbose_name='discount')
    def __str__(self):
        return str(self.discount)


class ItemDiscount(models.Model):
    """Item Discount"""
    days = models.ForeignKey(Days, on_delete=models.CASCADE, related_name='item_discount')
    dicounts = models.ForeignKey(Discount, on_delete=models.CASCADE, related_name='item_discount')

    def __str__(self):
        return f'{self.days}: {self.dicounts}'


class Delivery(models.Model):
    """Delivery"""
    city = models.PositiveIntegerField(default=0, verbose_name='price within the city')
    outside_city = models.PositiveIntegerField(verbose_name='price outside the city', null=True, blank=True)

    def __str__(self):
        if self.outside_city:
            return f'City:{self.city}, Outside:{self.outside_city}'
        return f'City:{self.city}'


class ProductImage(models.Model):
    """Product Images"""
    image = models.ImageField(upload_to='products')
    owner = models.ForeignKey(UserMode, on_delete=models.SET_NULL, null=True, limit_choices_to={'mode': '1'})

    def __str__(self):
        return f'{self.owner.client.username}: {self.id}'
    

class Product(models.Model):
    """Products"""
    CHOICES = [(i,i) for i in range(1, 11)]
    user = models.ForeignKey(UserMode, on_delete=models.SET_NULL, null=True, limit_choices_to={'mode': '1'})
    title = models.CharField(max_length=255)
    images = models.ManyToManyField(ProductImage, related_name='products')
    description = models.TextField(blank=True)
    price = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='products')
    subcategory = models.ForeignKey(Subcategory, on_delete=models.SET_NULL, null=True, blank=True, related_name='products')
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, blank=True, related_name='products')
    discount = models.ManyToManyField(ItemDiscount, related_name='products', blank=True)
    condition = models.IntegerField(choices=CHOICES, blank=True, null=True)
    purchase_price = models.PositiveIntegerField(blank=True, null=True)
    pledge = models.PositiveIntegerField(default=0)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, related_name='products')
    delivery = models.ForeignKey(Delivery, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='delivery price')
    pickup = models.CharField(max_length=800, blank=True, verbose_name='pickup address')

    def __str__(self):
        return self.title
    

class Favorite(models.Model):
    user = models.ForeignKey(UserMode,
        on_delete=models.CASCADE,
        related_name="favorites",
        limit_choices_to={'mode': '0'})
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.product.name}'


class ProductPromoteContract(models.Model):
    CHOICES = [(i,i) for i in range(1, 8)]
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_promote_contract')
    service = models.ForeignKey('ProductPromoteServicePrice', on_delete=models.CASCADE, related_name='product_promote_contract')
    period = models.IntegerField(choices=CHOICES)
    created_at = models.DateTimeField(editable=False)
    expired_date = models.DateTimeField(editable=False)
    total_price = models.PositiveIntegerField(editable=False)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = now()
            self.expired_date = self.created_at + timedelta(days=self.period)
            self.total_price = self.service.price_with_sale * self.period
        super(ProductPromoteContract, self).save(*args, **kwargs)
    
    def __str__(self):
        return f'{self.product.title}: {self.expired_date}'
        

class ProductPromoteService(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='promote_services/')
    max_places = models.IntegerField()

    @property
    def places_left(self):
        reserved_places = ProductPromoteContract.objects.filter(expired_at__gte=now()).count()
        return self.max_places - reserved_places


class ProductPromoteServicePrice(models.Model):
    product_promote_service = models.ForeignKey(ProductPromoteService, on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    price_with_sale = models.PositiveIntegerField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.price_with_sale:
            self.price_with_sale = self.price
        super(ProductPromoteServicePrice, self).save(*args, **kwargs)
    
    def __str__(self):
        return f'{self.product_promote_service}: {self.price_with_sale}'