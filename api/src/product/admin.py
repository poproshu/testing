from django.contrib import admin
from product import models
# Register your models here.



admin.site.register(models.Product)
admin.site.register(models.Category)
admin.site.register(models.City)
admin.site.register(models.Days)
admin.site.register(models.Brand)
admin.site.register(models.Subcategory)
admin.site.register(models.ItemDiscount)
admin.site.register(models.Discount)

