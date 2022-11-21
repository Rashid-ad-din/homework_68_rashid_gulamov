from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import DetailView, CreateView, ListView, UpdateView
from webapp.models import Vacancies
from accounts.models import Account
from webapp.forms.vacancies import VacancyForm


class ListVacancyView(LoginRequiredMixin, ListView):
    template_name = 'vacancies/vacancies.html'
    model = Vacancies

    def get(self, request, *args, **kwargs):
        vacancy_pk = request.GET.get('vacancy_pk')

        activate = request.GET.get('activate')
        if activate:
            vacancy = get_object_or_404(Vacancies, pk=vacancy_pk)
            vacancy.is_hidden = 0
            vacancy.save()

        deactivate = request.GET.get('deactivate')
        if deactivate:
            vacancy = get_object_or_404(Vacancies, pk=vacancy_pk)
            vacancy.is_hidden = 1
            vacancy.save()
        self.user_obj = get_object_or_404(Account, pk=kwargs.get('pk'))
        return super(ListVacancyView, self).get(request, *args, **kwargs)

    def get_queryset(self, **kwargs):
        queryset = Vacancies.objects.filter(author_id=self.request.user.pk)
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['user_obj'] = self.user_obj
        return context


class CreateVacancyView(LoginRequiredMixin, CreateView):
    template_name = 'vacancies/create_vacancy.html'
    model = Vacancies
    form_class = VacancyForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            resume = form.save(commit=False)
            resume.author = request.user
            resume.save()
            return redirect('profile', pk=self.request.user.pk)
        context = {}
        context['form'] = form
        return self.render_to_response(context)

    def get_success_url(self):
        return reverse('profile', kwargs={'pk': self.request.user.pk})


class VacancyView(LoginRequiredMixin, DetailView):
    template_name = 'vacancies/vacancy.html'
    model = Vacancies
    context_object_name = 'vacancy'


class EditVacancyView(LoginRequiredMixin, UpdateView):
    template_name = 'vacancies/edit_vacancy.html'
    model = Vacancies
    form_class = VacancyForm

    def get_success_url(self):
        return reverse('vacancy', kwargs={'upk': self.request.user.pk, 'pk': self.object.pk})
