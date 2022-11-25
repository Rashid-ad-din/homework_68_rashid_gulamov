from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import DetailView, CreateView, ListView, UpdateView, DeleteView
from webapp.models import Vacancies
from accounts.models import Account
from webapp.forms.vacancies import VacancyForm
from webapp.models import Resumes
from webapp.models import Respond


class ListVacancyView(LoginRequiredMixin, ListView):
    template_name = 'vacancies/vacancies.html'
    model = Vacancies

    def get(self, request, pk, *args, **kwargs):
        self.user_obj = get_object_or_404(Account, pk=pk)
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
        refresh = request.GET.get('refresh')
        if refresh:
            vacancy = get_object_or_404(Vacancies, pk=vacancy_pk)
            vacancy.save()
        return super(ListVacancyView, self).get(request, *args, **kwargs)

    def get_queryset(self, **kwargs):
        queryset = Vacancies.objects.filter(author_id=self.request.user.pk).order_by('-updated_at')
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['user_obj'] = self.user_obj
        return context


class CreateVacancyView(PermissionRequiredMixin, CreateView):
    template_name = 'vacancies/create_vacancy.html'
    model = Vacancies
    form_class = VacancyForm
    permission_required = 'webapp.add_vacancies'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            resume = form.save(commit=False)
            resume.author = request.user
            resume.save()
            return redirect('vacancies', pk=self.request.user.pk)
        context = {}
        context['form'] = form
        return self.render_to_response(context)

    def get_success_url(self):
        return reverse('vacancies', kwargs={'pk': self.request.user.pk})

    def has_permission(self):
        return super().has_permission() or self.request.user.is_superuser


class VacancyView(PermissionRequiredMixin, DetailView):
    template_name = 'vacancies/vacancy.html'
    model = Vacancies
    context_object_name = 'vacancy'
    permission_required = 'webapp.view_vacancies'

    def get(self, request, *args, **kwargs):
        vacancy = get_object_or_404(Vacancies, pk=kwargs.get('pk'))
        self.user_obj = vacancy.author
        refresh = request.GET.get('refresh')
        if refresh:
            vacancy.save()
        return super(VacancyView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        resumes = Resumes.objects.filter(author_id=self.request.user.pk, is_hidden="False")
        kwargs['resumes'] = resumes
        responds = Respond.objects.all()
        kwargs['responds'] = responds
        kwargs['user_obj'] = self.user_obj
        return super().get_context_data(**kwargs, form=VacancyForm())


class EditVacancyView(PermissionRequiredMixin, UpdateView):
    template_name = 'vacancies/edit_vacancy.html'
    model = Vacancies
    form_class = VacancyForm
    permission_required = 'webapp.change_vacancies'

    def get_success_url(self):
        return reverse('vacancy', kwargs={'upk': self.request.user.pk, 'pk': self.object.pk})

    def has_permission(self):
        return super().has_permission() and self.get_object().author == self.request.user \
               or self.request.user.is_superuser


class DeleteVacancyView(PermissionRequiredMixin, DeleteView):
    template_name = 'vacancies/delete_vacancy.html'
    model = Vacancies
    context_object_name = 'vacancy'
    permission_required = 'webapp.delete_vacancies'

    def get_success_url(self):
        return reverse('vacancies', kwargs={'pk': self.request.user.pk})

    def has_permission(self):
        return super().has_permission() and self.get_object().author == self.request.user \
               or self.request.user.is_superuser
