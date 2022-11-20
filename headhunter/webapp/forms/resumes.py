from django import forms

from webapp.models import Resumes


class ResumeForm(forms.ModelForm):

    class Meta:
        model = Resumes
        fields = ('name',
                  'last_name',
                  'position',
                  'category',
                  'salary',
                  'phone_number',
                  'email',
                  'telegram',
                  'facebook',
                  'linkedin',
                  'about_worker')