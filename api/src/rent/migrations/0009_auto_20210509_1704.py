# Generated by Django 3.0.5 on 2021-05-09 14:04

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0008_auto_20210506_2322'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='rent',
            name='start_date_can_be_the_next_day',
        ),
        migrations.AddConstraint(
            model_name='rent',
            constraint=models.CheckConstraint(check=models.Q(_negated=True, start_date__gt=datetime.datetime(2021, 5, 10, 14, 3, 49, 861592, tzinfo=utc)), name='start_date_can_be_the_next_day'),
        ),
    ]
