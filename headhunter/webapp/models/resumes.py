from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from webapp.managers import HHProjectManager
from webapp.models import BaseModel
from webapp.models.categories import CategoryChoices


class Resumes(BaseModel):
    author = models.ForeignKey(
        verbose_name='Автор *',
        to=get_user_model(),
        related_name='resumes',
        null=False,
        blank=False,
        on_delete=models.CASCADE
    )
    name = models.CharField(
        verbose_name="Имя *",
        max_length=100,
        null=False,
        blank=False
    )
    last_name = models.CharField(
        verbose_name="Фамилия *",
        max_length=100,
        null=False,
        blank=False
    )
    position = models.CharField(
        verbose_name="Позиция *",
        max_length=100,
        null=False,
        blank=False
    )
    category = models.CharField(
        verbose_name='Сфера деятельности',
        choices=CategoryChoices.choices,
        max_length=100,
        default=CategoryChoices.OTHER
    )
    salary = models.IntegerField(
        null=False,
        blank=False,
        verbose_name='Уровень дохода *',
        validators=[
            MinValueValidator(0),
            MaxValueValidator(1000000000)
        ]
    )
    phone_number = models.CharField(
        max_length=20,
        null=False,
        blank=False,
        verbose_name='Телефон *'

    )
    email = models.EmailField(
        verbose_name='Email *',
        unique=False,
        null=False,
        blank=False,
    )
    telegram = models.URLField(
        max_length=200,
        null=False,
        blank=False,
        verbose_name='Telegram *'
    )
    facebook = models.URLField(
        max_length=200,
        null=True,
        blank=True,
        verbose_name='Facebook'
    )
    linkedin = models.URLField(
        max_length=200,
        null=True,
        blank=True,
        verbose_name='Linkedin'
    )
    experience = models.ManyToManyField(
        verbose_name='Опыт работы',
        to='webapp.Experiences',
        related_name='worker_experience',
        blank=True
    )
    education = models.ManyToManyField(
        verbose_name='Образование',
        to='webapp.Educations',
        related_name='worker_education',
        blank=True
    )
    about_worker = models.TextField(
        verbose_name="Обо мне",
        blank=True,
        null=True
    )
    is_hidden = models.BooleanField(
        verbose_name='Активность резюме',
        default=False,
        null=False
    )

    objects = HHProjectManager()

    def __str__(self):
        return f"{self.name}"

    class Meta:
        db_table = "resume"
        verbose_name = "Резюме"
        verbose_name_plural = "Резюме"
