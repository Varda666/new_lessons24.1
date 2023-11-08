# Generated by Django 4.2.7 on 2023-11-08 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Название курса')),
                ('img', models.ImageField(upload_to='media/', verbose_name='Картинка')),
                ('description', models.TextField(max_length=500, verbose_name='Описание курса')),
            ],
            options={
                'verbose_name': 'курс',
                'verbose_name_plural': 'курсы',
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Название урока')),
                ('img', models.ImageField(upload_to='media/', verbose_name='Картинка')),
                ('description', models.TextField(max_length=500, verbose_name='Описание урока')),
                ('link', models.CharField(max_length=300, verbose_name='Ссылка на видео')),
            ],
            options={
                'verbose_name': 'урок',
                'verbose_name_plural': 'уроки',
            },
        ),
    ]
