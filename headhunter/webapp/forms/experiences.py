from django import forms
from django.forms import TextInput

from webapp.models import Experiences


class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experiences
        fields = (
            'name_of_company',
            'experience',
            'start_date',
            'end_date',
            'position',
            'responsibilities',
            'additional_info',
        )
        widgets = {
            'start_date': TextInput(attrs={
                'class': 'form-control',
                'style': 'max-width: 400px;',
                'type': 'date',
            }),
            'end_date': TextInput(attrs={
                'class': 'form-control',
                'style': 'max-width: 400px;',
                'type': 'date',
            })
        }
