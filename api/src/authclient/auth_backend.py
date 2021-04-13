from django.db.models import Q
from customuser.models import Client


def authenticate(username=None, password=None, **kwargs):
    if Client.objects.filter(Q(username=username) | Q(email=username)).exists():
        client = Client.objects.filter(Q(username=username) | Q(email=username)).last()
        if client.check_password(password):
            return client

    return None
