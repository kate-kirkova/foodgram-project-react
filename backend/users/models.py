from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = models.CharField(
        db_index=True,
        max_length=150,
        unique=True,
        verbose_name='Логин',
        help_text='Введите логин')
    email = models.EmailField(
        db_index=True,
        unique=True,
        max_length=254,
        verbose_name='Электронная почта',
        help_text='Введите электронную почту')
    first_name = models.CharField(
        max_length=150,
        verbose_name='Имя',
        help_text='Введите имя')
    last_name = models.CharField(
        max_length=150,
        verbose_name='Фамилия',
        help_text='Введите фамилию')
    is_subscribed = models.BooleanField(
        default=False,
        verbose_name='Подписка на пользователя',
        help_text='Отметьте, чтобы подписаться на пользователя')
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'password']

    def __str__(self):
        return self.username
