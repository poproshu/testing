from django.contrib import admin
from customuser.models import User, Client, Staff

admin.site.register(User)

admin.site.register(Client)

admin.site.register(Staff)