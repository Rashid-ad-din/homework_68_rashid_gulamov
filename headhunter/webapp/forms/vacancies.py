from django import forms
from webapp.models import Vacancies


class VacancyForm(forms.ModelForm):
    class Meta:
        model = Vacancies
        fields = ('position',
                  'category',
                  'salary',
                  'description',
                  'min_experience',
                  'max_experience',
                  )
