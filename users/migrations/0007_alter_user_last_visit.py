# Generated by Django 4.2.7 on 2023-12-08 15:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_user_last_visit_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='last_visit',
            field=models.DateField(default=datetime.datetime(2023, 12, 8, 18, 4, 9, 578189), verbose_name='Дата последнего посещения'),
        ),
    ]
