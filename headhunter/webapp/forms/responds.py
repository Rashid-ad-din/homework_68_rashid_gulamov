from django import forms
from django.forms import Textarea

from webapp.models import Respond, RespondMessage


class RespondForm(forms.ModelForm):
    class Meta:
        model = Respond
        fields = ('vacancy',
                  'resume',
                  )


class RespondMessageForm(forms.ModelForm):
    class Meta:
        model = RespondMessage
        fields = ('text',)
        labels = {'text': ''}
        widgets = {
            'text': Textarea(attrs={
                'rows': 4,
                'cols': 38,
                'placeholder': 'Добавьте сообщение',
                'class': 'border-0 border-top rounded',
                'style': 'outline:0px none transparent; overflow:auto; resize:none',
            })
        }