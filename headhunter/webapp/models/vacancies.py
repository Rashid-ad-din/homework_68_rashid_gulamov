from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from webapp.models import BaseModel
from webapp.managers import HHProjectManager
from webapp.models.categories import CategoryChoices


class Vacancies(BaseModel):
    author = models.ForeignKey(
        verbose_name='Автор',
        to=get_user_model(),
        related_name='vacancies',
        null=False,
        blank=False,
        on_delete=models.CASCADE
    )
    position = models.CharField(
        verbose_name="Позиция",
        max_length=100,
        null=False,
        blank=False
    )
    category = models.CharField(
        verbose_name='Категория',
        choices=CategoryChoices.choices,
        max_length=100,
        default=CategoryChoices.OTHER
    )
    salary = models.IntegerField(
        null=False,
        blank=False,
        verbose_name='Уровень дохода',
        validators=[
            MinValueValidator(0),
            MaxValueValidator(1000000000)
        ]
    )
    description = models.TextField(
        verbose_name="Описание",
        blank=True,
        null=True
    )
    min_experience = models.IntegerField(
        null=False,
        blank=False,
        verbose_name='Минимальный опыт',
        validators=[
            MinValueValidator(0),
            MaxValueValidator(50)
        ]
    )
    max_experience = models.IntegerField(
        null=False,
        blank=False,
        verbose_name='Максимальный опыт',
        validators=[
            MinValueValidator(0),
            MaxValueValidator(50)
        ]
    )
    is_hidden = models.BooleanField(
        verbose_name='Активность вакансии',
        default=False,
        null=False
    )
    resumes = models.ManyToManyField(
        verbose_name='Резюме',
        to='webapp.Resumes',
        related_name='worker_resume',
        blank=True
    )

    objects = HHProjectManager()

    def __str__(self):
        return f"{self.position}"

    class Meta:
        db_table = "vacancy"
        verbose_name = "Вакансия"
        verbose_name_plural = "Вакансии"
