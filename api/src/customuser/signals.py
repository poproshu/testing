from .models import Client, UserMode
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=Client)
def create_mode(sender, instance, created, **kwargs):
    if created:
        UserMode.objects.create(client=instance, mode='0')
        UserMode.objects.create(client=instance, mode='1') 