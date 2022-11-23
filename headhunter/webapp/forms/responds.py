from django import forms
from webapp.models import Respond


class RespondForm(forms.ModelForm):
    class Meta:
        model = Respond
        fields = ('vacancy',
                  'resume',
                  )
