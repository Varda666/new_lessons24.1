# Generated by Django 4.2.7 on 2023-12-25 19:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_alter_user_last_visit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='last_visit',
            field=models.DateField(default=datetime.datetime(2023, 12, 25, 22, 43, 23, 353904), verbose_name='Дата последнего посещения'),
        ),
    ]
