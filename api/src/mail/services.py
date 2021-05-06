from django.core.mail import EmailMessage
from config.settings.base import SERVICE_EMAIL


def send_email(email, name, phone, message):
    email = EmailMessage(
        'POPROSHU SERVICE: USER MESSAGE',
        f'user: {name}, email: {email}, phone: {phone}, message: {message}',
        'djangoemailsend@gmail.com',
        [SERVICE_EMAIL,],
    )
    email.send(fail_silently=True)