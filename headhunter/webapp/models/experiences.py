from django.db import models
from webapp.models import BaseModel


class Experiences(BaseModel):
    name_of_company = models.CharField(
        verbose_name="Компания",
        max_length=100,
        null=False,
        blank=False
    )
    experience = models.DecimalField(
        null=False,
        blank=False,
        max_digits=5,
        decimal_places=2,
        verbose_name='Стаж')
    start_date = models.TextField(
        verbose_name="Дата начала",
        blank=True,
        null=True
    )
    end_date = models.TextField(
        verbose_name="Дата увольнения",
        blank=True,
        null=True
    )
    position = models.CharField(
        verbose_name="Позиция",
        max_length=100,
        null=False,
        blank=False
    )
    responsibilities = models.TextField(
        verbose_name="Обязанности",
        blank=False,
        null=False
    )
    additional_info = models.TextField(
        verbose_name="Дополнительная информация",
        blank=True,
        null=True
    )

    def __str__(self):
        return f"{self.name_of_company}"

    class Meta:
        db_table = "experience"
        verbose_name = "Опыт работы"
        verbose_name_plural = "Опыт работы"
