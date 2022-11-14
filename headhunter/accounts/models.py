from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import TextChoices


class GenderChoices(TextChoices):
    COMPANY = 'company', 'Компания'
    USER = 'candidate', 'Кандидат'


class Account(AbstractUser):
    usertype = models.CharField(choices=GenderChoices.choices, verbose_name='Пользователь', null=False,
                                blank=False, max_length=250)
    username = models.CharField(verbose_name='Имя', unique=True, null=False, blank=False, max_length=150)
    email = models.EmailField(verbose_name='Электронная почта', unique=True, null=False, blank=False)
    avatar = models.ImageField(
        null=True,
        blank=True,
        upload_to='avatars',
        verbose_name='Аватар'
    )
    phone = models.CharField(verbose_name='Телефона', null=False, blank=False, max_length=100)

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
