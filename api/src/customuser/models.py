from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db.models import Q, F
from django.db import models


class UserManager(BaseUserManager):

    def get_by_natural_key(self, email):
        return self.get(email=email)

    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        defaultuser = User(email=email, **extra_fields)
        defaultuser.set_password(password)
        defaultuser.save()

        return defaultuser


class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(db_index=True, unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'

    objects = UserManager()

    def get_full_name(self):
        return (self.first_name + ' ' + self.last_name)

    def get_short_name(self):
        return self.first_name

    def natural_key(self):
        return (self.first_name, self.last_name)

    def __str__(self):
        return self.email


class StaffManager(BaseUserManager):

    def create_staff(self, email, password=None):
        if email is None:
            raise TypeError('Users must have an email address.')
        staff = Staff(email=self.normalize_email(email), is_staff=True)
        staff.set_password(password)
        staff.save()
        return client


class Staff(User, PermissionsMixin):
    avatar = models.ImageField(upload_to='images/avatars/', null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = StaffManager()

    def __str__(self):
        return self.email


class ClientManager(BaseUserManager):

    def create_client(self, username, email, password=None):
        if email is None:
            raise TypeError('Users must have an email.')
        if username is None:
            raise TypeError('Users must have an username.')
        client = Client(username=username, email=email)
        client.set_password(password)
        client.save()
        return client


class City(models.Model):
    city = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.city


class Address(models.Model):
    street = models.CharField(max_length=255)
    house = models.CharField(max_length=255)
    flat_number = models.CharField(max_length=255, blank=True)
    floor = models.IntegerField(blank=True)
    entrance_number = models.CharField(max_length= 255, blank=True)
    intercome_code = models.CharField(max_length=255, blank=True)  

    def __str__(self):
        return f'{self.street}, {self.house}'


class Client(User, PermissionsMixin):
    address = models.ManyToManyField(Address, blank=True, related_name='user')
    username = models.CharField(max_length=100, unique=True)
    phone = models.CharField(max_length=11, blank=True)
    avatar = models.ImageField(upload_to='images/avatar/', blank=True, null=True)
    # favorite = 
    # passport
    birth_date = models.DateField(blank=True, null=True)
    user_city = models.ForeignKey(City, blank=True, null=True, on_delete=models.SET_NULL)
    is_subscribed = models.BooleanField(default=False)
    email_notification = models.BooleanField(default=False)
    tg_notification = models.BooleanField(default=False)
    phone_notification = models.BooleanField(default=False)
    ws_notification = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = ClientManager()

    def __str__(self):
        return self.username


class UserMode(models.Model):
    # Устанавливаем варианты режимов для пользователя
    MODE = [('0', 'Get'),('1', 'Give')]
    mode = models.CharField(max_length=10, choices=MODE)
    # Устанавливаем связь между режимами и юзером
    client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE
    )

    class Meta:
        unique_together = ('mode', 'client')

    def __str__(self):
        return f'User:{self.client}, Mode: {self.mode}'


class Comment(models.Model):
    # Владелец комментария 
    comment_owner = models.ForeignKey(
        UserMode,
        on_delete=models.SET_NULL,
        null=True,
        related_name="comment_owner"
    )
    # Получатель комментария 
    comment_reciever = models.ForeignKey(
        UserMode,
        on_delete=models.SET_NULL,
        null=True,
        related_name="comment_reciever"
    )
    # Сообщение комментария 
    comment_body = models.TextField(max_length=370)

    def __str__(self):
        return str(self.comment_reciever)
        