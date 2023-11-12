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
    country = models.CharField(max_length=150, verbose_name='Номер телефона')
    img = models.ImageField(upload_to='media/', default=None, verbose_name='Аватар')



    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []