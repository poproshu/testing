from django.apps import AppConfig


class CustomUserConfig(AppConfig):
    name = 'customuser'

    def ready(self):
        from . import signals
