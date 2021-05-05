from django.core.mail import EmailMessage
from django.utils.crypto import get_random_string
from authclient.models import EmailCode


def send_code_by_email(user):
    code = get_random_string(length=12)
    email = EmailMessage(
        'POPROSHU SERVICE: Email verification',
        f'Your code: {code}',
        'djangoemailsend@gmail.com',
        [user.email],
    )
    email.send(fail_silently=True)
    EmailCode.objects.create(client=user, code=code)
