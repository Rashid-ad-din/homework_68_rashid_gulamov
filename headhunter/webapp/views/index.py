from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from webapp.models import Resumes


# Create your views here.
class IndexView(ListView):
    template_name = 'resumes/resumes.html'
    model = Resumes

    def get_queryset(self):
        queryset = Resumes.objects.filter(is_hidden=False)
        return queryset
