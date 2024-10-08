from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    """Класс для описания модели Пользователь"""
    ROLES = (('teacher', 'teacher'), ('student', 'student'))
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')
    first_name = models.CharField(max_length=50, **NULLABLE, verbose_name='Имя')
    last_name = models.CharField(max_length=50, **NULLABLE, verbose_name='Фамилия')
    phone = models.CharField(max_length=35, verbose_name='телефон', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)
    tg_chat_id = models.CharField(max_length=50, verbose_name='telegram chat_id', **NULLABLE)
    token = models.CharField(max_length=100, verbose_name='token', **NULLABLE)
    is_active = models.BooleanField(default=True, verbose_name='Статус активности')
    role = models.CharField(max_length=100, choices=ROLES, **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'