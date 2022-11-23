from django import forms
from django.forms import TextInput

from webapp.models import Educations


class EducationForm(forms.ModelForm):
    class Meta:
        model = Educations
        fields = (
            'name',
            'start_date',
            'end_date',
            'speciality',
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
