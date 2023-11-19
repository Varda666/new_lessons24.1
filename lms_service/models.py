from django.contrib.auth.models import AbstractUser
from django.db import models

import users


# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название курса', unique=True)
    img = models.ImageField(upload_to='media/', default=None, verbose_name='Картинка')
    description = models.TextField(max_length=500, verbose_name='Описание курса')
    lessons_count = models.IntegerField(default=0, verbose_name='количество уроков в курсе')
    user = models.ForeignKey(to='users.User', to_field='email', default=None, verbose_name='владелец', on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'

class Lesson(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название урока', unique=True)
    img = models.ImageField(upload_to='media/', default=None, verbose_name='Картинка')
    description = models.TextField(max_length=500, verbose_name='Описание урока')
    link = models.URLField(verbose_name='Ссылка на видео')
    course = models.ForeignKey(to='Course', to_field='name', default=None, verbose_name='курс', on_delete=models.PROTECT)
    user = models.ForeignKey(to='users.User', to_field='email', default=None, verbose_name='владелец', on_delete=models.PROTECT)


    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'

class Payment(models.Model):
    transfer = 'transfer to the account'
    PAYMENT_METHOD_CHOISES = [
        ('cash', 'cash'),
        ('transfer', 'transfer to the account')
    ]
    user = models.ForeignKey(to='users.User', to_field='email', verbose_name='плательщик', on_delete=models.PROTECT)
    pay_date = models.DateField(verbose_name='дата оплаты')
    paid_course = models.ForeignKey(to='Course', to_field='name', verbose_name='оплаченный курс', blank=True, null=True, on_delete=models.PROTECT)
    paid_lesson = models.ForeignKey(to='Lesson', to_field='name', verbose_name='оплаченный урок', blank=True, null=True, on_delete=models.PROTECT)
    payment_amount = models.PositiveIntegerField(verbose_name='сумма оплаты')
    payment_method = models.CharField(choices=PAYMENT_METHOD_CHOISES, default=transfer, verbose_name='способ оплаты')

    class Meta:
        constraints = (
            models.CheckConstraint(
                check=models.Q(paid_course__isnull=False) & models.Q(paid_lesson__isnull=False),
                name='course_lesson_not_null'
            ),
        )


