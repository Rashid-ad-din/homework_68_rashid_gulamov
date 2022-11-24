from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from accounts.models import Account
from webapp.forms.resumes import ResumeForm
from webapp.models import Respond, Resumes, Vacancies


class CreateResumeView(PermissionRequiredMixin, CreateView):
    template_name = 'resumes/create_resume.html'
    model = Resumes
    form_class = ResumeForm
    permission_required = 'webapp.add_resumes'

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

    def has_permission(self):
        return super().has_permission() or self.request.user.is_superuser


class ListResumesView(LoginRequiredMixin, ListView):
    template_name = 'resumes/resumes.html'
    model = Resumes

    def get(self, request, pk, *args, **kwargs):
        self.user_obj = get_object_or_404(Account, pk=pk)
        resume_pk = request.GET.get('resume_pk')
        activate = request.GET.get('activate')
        if activate:
            resume = get_object_or_404(Resumes, pk=request.GET.get('resume_pk'))
            resume.is_hidden = 0
            resume.save()
        deactivate = request.GET.get('deactivate')
        if deactivate:
            resume = get_object_or_404(Resumes, pk=request.GET.get('resume_pk'))
            resume.is_hidden = 1
            resume.save()
        refresh = request.GET.get('refresh')
        if refresh:
            resume = get_object_or_404(Resumes, pk=request.GET.get('resume_pk'))
            resume.save()
        return super(ListResumesView, self).get(request, *args, **kwargs)

    def get_queryset(self, **kwargs):
        queryset = Resumes.objects.filter(author_id=self.request.user.pk).order_by('-updated_at')
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['user_obj'] = self.user_obj
        return context


class ResumeView(LoginRequiredMixin, DetailView):
    template_name = 'resumes/resume.html'
    model = Resumes
    context_object_name = 'resume'

    def get(self, request, *args, **kwargs):
        res = get_object_or_404(Resumes, pk=kwargs.get('pk'))
        self.user_obj = res.author
        refresh = request.GET.get('refresh')
        if refresh:
            resume = get_object_or_404(Resumes, pk=kwargs.get('pk'))
            resume.save()
        return super(ResumeView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        vacancy = Vacancies.objects.filter(author_id=self.request.user.pk, is_hidden="False")
        kwargs['vacancies'] = vacancy
        responds = Respond.objects.all()
        kwargs['responds'] = responds
        kwargs['user_obj'] = self.user_obj
        return super().get_context_data(**kwargs, form=ResumeForm())


class EditResumeView(PermissionRequiredMixin, UpdateView):
    template_name = 'resumes/edit_resume.html'
    model = Resumes
    form_class = ResumeForm
    permission_required = 'webapp.change_resumes'

    def get_success_url(self):
        return reverse('resume', kwargs={'pk': self.object.pk})

    def has_permission(self):
        return super().has_permission() and self.get_object().author == self.request.user \
               or self.request.user.is_superuser


class DeleteResumeView(PermissionRequiredMixin, DeleteView):
    template_name = 'resumes/delete_resume.html'
    model = Resumes
    context_object_name = 'resume'
    permission_required = 'webapp.delete_resumes'

    def get_success_url(self):
        return reverse('resumes', kwargs={'pk': self.request.user.pk})

    def has_permission(self):
        return super().has_permission() and self.get_object().author == self.request.user \
               or self.request.user.is_superuser
