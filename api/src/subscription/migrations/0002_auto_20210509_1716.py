# Generated by Django 3.0.5 on 2021-05-09 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='subscribed_at',
            field=models.DateField(editable=False),
        ),
    ]
