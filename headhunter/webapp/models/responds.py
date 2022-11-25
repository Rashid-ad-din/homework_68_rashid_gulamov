from django.contrib.auth import get_user_model
from django.db import models


class Respond(models.Model):
    resume = models.ForeignKey(
        verbose_name='Резюме',
        to='webapp.Resumes',
        on_delete=models.CASCADE,
        related_name='respond_resume'
    )
    vacancy = models.ForeignKey(
        verbose_name='Вакансия',
        to='webapp.Vacancies',
        on_delete=models.CASCADE,
        related_name='respond_vacancy'
    )

    def __str__(self):
        return f"{self.resume} {self.vacancy}"

    class Meta:
        verbose_name = "Отклик"
        verbose_name_plural = "Отклики"


class RespondMessage(models.Model):
    respond = models.ForeignKey(
        verbose_name='Отклик',
        to='webapp.Respond',
        on_delete=models.CASCADE,
        related_name='respond_message'
    )
    author = models.ForeignKey(
        verbose_name='Автор',
        to=get_user_model(),
        related_name='messages',
        null=False,
        blank=False,
        on_delete=models.CASCADE
    )
    text = models.CharField(
        verbose_name='Текст сообщения',
        max_length=3000,
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Запись создана'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Запись изменена'
    )
