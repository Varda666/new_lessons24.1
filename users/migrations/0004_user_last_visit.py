# Generated by Django 4.2.7 on 2023-12-05 20:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_user_country_usersubscriptionupdates'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='last_visit',
            field=models.DateField(default=datetime.datetime(2023, 12, 5, 23, 41, 56, 130881), verbose_name='Дата последнего посещения'),
        ),
    ]
