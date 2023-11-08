from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название курса')
    img = models.ImageField(upload_to='media/', verbose_name='Картинка')
    description = models.TextField(max_length=500, verbose_name='Описание курса')

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'

class Lesson(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название урока')
    img = models.ImageField(upload_to='media/', verbose_name='Картинка')
    description = models.TextField(max_length=500, verbose_name='Описание урока')
    link = models.CharField(max_length=300, verbose_name='Ссылка на видео')


    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'