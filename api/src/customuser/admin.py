from django.contrib import admin
from customuser.models import User, Client, Staff, UserMode

admin.site.register(User)

admin.site.register(Client)

admin.site.register(Staff)

admin.site.register(UserMode)