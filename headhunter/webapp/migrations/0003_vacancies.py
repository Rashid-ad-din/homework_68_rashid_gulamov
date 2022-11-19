# Generated by Django 4.1.3 on 2022-11-19 17:45

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('webapp', '0002_delete_vacancies'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vacancies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('position', models.CharField(max_length=100, verbose_name='Позиция')),
                ('category', models.CharField(choices=[('other', 'Другое'), ('medicine', 'Медицина'), ('it', 'Информационные технологии'), ('marketing', 'Маркетинг'), ('science', 'Наука')], default='other', max_length=100, verbose_name='Категория')),
                ('salary', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1000000000)], verbose_name='Уровень дохода')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('min_experience', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(50)], verbose_name='Минимальный опыт')),
                ('max_experience', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(50)], verbose_name='Максимальный опыт')),
                ('is_hidden', models.BooleanField(default=False, verbose_name='Активность вакансии')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vacancies', to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
                ('resumes', models.ManyToManyField(blank=True, related_name='worker_resume', to='webapp.resumes', verbose_name='Резюме')),
            ],
            options={
                'verbose_name': 'Вакансия',
                'verbose_name_plural': 'Вакансии',
                'db_table': 'vacancy',
            },
        ),
    ]
