from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView

from accounts.models import Account
from webapp.forms.resumes import ResumeForm
from webapp.models import Resumes
from webapp.models import Respond
from webapp.models import Vacancies


class CreateResumeView(LoginRequiredMixin, CreateView):
    template_name = 'resumes/create_resume.html'
    model = Resumes
    form_class = ResumeForm

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


class ListResumesView(LoginRequiredMixin, ListView):
    template_name = 'resumes/resumes.html'
    model = Resumes

    def get(self, request, *args, **kwargs):
        resume_pk = request.GET.get('resume_pk')

        activate = request.GET.get('activate')
        if activate:
            resume = get_object_or_404(Resumes, pk=resume_pk)
            resume.is_hidden = 0
            resume.save()

        deactivate = request.GET.get('deactivate')
        if deactivate:
            resume = get_object_or_404(Resumes, pk=resume_pk)
            resume.is_hidden = 1
            resume.save()
        self.user_obj = get_object_or_404(Account, pk=kwargs.get('pk'))
        return super(ListResumesView, self).get(request, *args, **kwargs)

    def get_queryset(self, **kwargs):
        queryset = Resumes.objects.filter(author_id=self.request.user.pk)
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['user_obj'] = self.user_obj
        return context


class ResumeView(LoginRequiredMixin, DetailView):
    template_name = 'resumes/resume.html'
    model = Resumes
    context_object_name = 'resume'

    def get_context_data(self, **kwargs):
        vacancy = Vacancies.objects.filter(author_id=self.request.user.pk, is_hidden="False")
        kwargs['vacancies'] = vacancy
        responds = Respond.objects.all()
        kwargs['responds'] = responds
        return super().get_context_data(**kwargs, form=ResumeForm())


class EditResumeView(LoginRequiredMixin, UpdateView):
    template_name = 'resumes/edit_resume.html'
    model = Resumes
    form_class = ResumeForm

    def get_success_url(self):
        return reverse('resume', kwargs={'pk': self.object.pk})
