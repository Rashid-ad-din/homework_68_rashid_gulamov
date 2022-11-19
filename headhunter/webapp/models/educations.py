from django.db import models
from webapp.models import BaseModel


class Educations(BaseModel):
    name = models.CharField(
        verbose_name="Наименование образовательного учреждения",
        max_length=100,
        null=False,
        blank=False
    )
    start_date = models.TextField(
        verbose_name="Дата начала обучения",
        blank=False,
        null=False
    )
    end_date = models.TextField(
        verbose_name="Дата окончания обучения",
        blank=False,
        null=False
    )
    speciality = models.CharField(
        verbose_name="Специальность",
        max_length=100,
        null=False,
        blank=False
    )
    additional_info = models.TextField(
        verbose_name="Дополнительная информация",
        blank=True,
        null=True
    )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        db_table = "education"
        verbose_name = "Образование"
        verbose_name_plural = "Образование"
