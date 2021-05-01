from datetime import timedelta
from django.utils import timezone
from django.db.models import Q, F
from django.db import models
from product.models import Product
from customuser.models import UserMode


class Rent(models.Model):

    class StatusChoices(models.TextChoices):
        rent_request = 'Rent Request'
        approval_from_owner = 'Approval' #После одобрения открывается доступ к заполнению контракта и мы отслылаем письмо
        contract_signed = 'Contract signed'  
        # money_reserved = 'Money reserved'
        rent_started = 'Rent Started'
        rent_finished = 'Rent Finished'
        abort = 'Rent aborted'
    
    class PaymentChoices(models.TextChoices):
        card = 'Card'
        cash = 'Cash'

    owner = models.ForeignKey(
        UserMode,
        on_delete=models.SET_NULL,
        null=True,
        related_name="rent_owner"
    )
    receiver = models.ForeignKey(
        UserMode,
        on_delete=models.SET_NULL,
        null=True,
        related_name="rent_reciever"
    )
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    # payment_method = models.CharField(choices=PaymentChoices.choices, max_length=255)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    contract = models.FileField(upload_to='contracts/', null=True)
    status = models.CharField(choices=StatusChoices.choices, default=StatusChoices.rent_request, max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
        models.CheckConstraint(
            check=~Q(owner=F('receiver')),
            name='receiver_and_owner_can_not_be_equal'),
        models.CheckConstraint(
            check=~Q(start_date__gt=(F('end_date') + timedelta(days=1))),
            name='start_date_gt_end_date_plus_1_day'),
        models.CheckConstraint(
            check=~Q(start_date__gt=(timezone.now() + timedelta(days=1))),
            name='start_date_can_be_the_next_day'),
        ]
    # Когда устанавливается старт дейт
    # Что делать, если человек не возвращает в срок
    # Минимальная дата старт дейта

    def __str__(self):
        return f'{self.owner}: {self.receiver}'