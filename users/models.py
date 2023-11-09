from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='email')
    first_name = models.CharField(max_length=150, verbose_name='имя')
    last_name = models.CharField(max_length=150, verbose_name='фамилия')
    phone = models.CharField(max_length=35, verbose_name='Номер телефона')
    country = models.CharField(max_length=150, verbose_name='Номер телефона')
    img = models.ImageField(upload_to='media/', default=None, verbose_name='Аватар')



    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []