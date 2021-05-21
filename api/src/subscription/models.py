from datetime import timedelta
from django.utils.timezone import now
from django.db import models
from customuser.models import UserMode


class Subscription(models.Model):
    class PeriodChoices(models.TextChoices):
        month = 'month'
        six_month = 'six_month'
        yead = 'year'
    user = models.OneToOneField(UserMode, on_delete=models.SET_NULL, null=True, limit_choices_to={'mode': '1'}, related_name='subscription')
    period = models.CharField(max_length=20, choices=PeriodChoices.choices)
    subscribed_at = models.DateField(editable=False)
    expires_at = models.DateField(null=True, blank=True)
    
    @property
    def is_subscribed(self):
        return self.expires_at >= now().date()
    
    def duration(self):
        if self.period == 'six_month':
            return 30*6
        elif self.period == 'year':
            return 365
        else:
            return 30

    def save(self, *args, **kwargs):
        if not self.id:
            self.subscribed_at = now().date()
            self.expires_at = self.subscribed_at + timedelta(days=self.duration())
        super(Subscription, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.user.client.username}: expires_at {self.expires_at}'
        