# Generated by Django 3.0.5 on 2021-05-09 14:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customuser', '0008_client_sex'),
        ('subscription', '0002_auto_20210509_1716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='user',
            field=models.OneToOneField(limit_choices_to={'mode': '1'}, null=True, on_delete=django.db.models.deletion.SET_NULL, to='customuser.UserMode'),
        ),
    ]