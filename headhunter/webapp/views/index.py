from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from webapp.models import Resumes, Vacancies


class IndexView(ListView):
    template_name = 'vacancies/vacancies_list.html'
    model = Vacancies
    ordering = ('-updated_at',)
    context_object_name = 'vacancies'
    paginate_by = 20

    def get_context_data(self, *, object_list=None, **kwargs):
        kwargs['resumes'] = Resumes.objects.all().order_by('-updated_at')
        return super().get_context_data(**kwargs)

# class IndexView(ListView):
#     template_name = 'resumes/resumes.html'
#     model = Resumes
#
#     def get_queryset(self):
#         queryset = Resumes.objects.filter(is_hidden=False)
#         return queryset
