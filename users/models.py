from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    member = 'member'
    USER_ROLE_CHOISES = [
        ('member', 'member'),
        ('moderator', 'moderator')
    ]

    username = None
    user_role = models.CharField(choices=USER_ROLE_CHOISES, default=member, verbose_name='роль')
    email = models.EmailField(unique=True, verbose_name='email')
    first_name = models.CharField(max_length=150, verbose_name='имя')
    last_name = models.CharField(max_length=150, verbose_name='фамилия')
    phone = models.CharField(max_length=35, verbose_name='Номер телефона')
    country = models.CharField(max_length=150, verbose_name='страна')
    img = models.ImageField(upload_to='media/', default=None, verbose_name='Аватар')



    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class UserSubscriptionUpdates(models.Model):
    status = models.BooleanField(default=False, verbose_name="статус подписки")
    user = models.ForeignKey(to='User', to_field='email', verbose_name='пользователь', on_delete=models.PROTECT)
    course = models.ForeignKey(to='lms_service.Course', to_field='name', default=None, verbose_name='курс', on_delete=models.PROTECT)