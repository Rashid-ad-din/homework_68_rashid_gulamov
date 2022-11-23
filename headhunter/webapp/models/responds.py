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


class RespondMessage(models.Model):
    respond = models.ForeignKey(
        verbose_name='Отклик',
        to='webapp.Respond',
        on_delete=models.CASCADE,
        related_name='respond_message'
    )
    message = models.ForeignKey(
        verbose_name='Сообщение',
        to='webapp.Message',
        on_delete=models.CASCADE,
        related_name='message_text'
    )


class Message(models.Model):
    author = models.ForeignKey(
        get_user_model(),
        verbose_name='Автор',
        on_delete=models.CASCADE,
        related_name='author'
    )
    text = models.CharField(
        verbose_name='Текст сообщения',
        max_length=3000,
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        blank=True
    )
