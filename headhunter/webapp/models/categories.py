from django.db.models import TextChoices


class CategoryChoices(TextChoices):
    OTHER = 'other', 'Другое'
    MEDICINE = 'medicine', 'Медицина'
    IT = 'it', 'Информационные технологии'
    MARKETING = 'marketing', 'Маркетинг'
    SCIENCE = 'science', 'Наука'
