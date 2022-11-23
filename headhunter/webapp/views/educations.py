from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import CreateView, UpdateView, DeleteView

from webapp.forms.educations import EducationForm
from webapp.models import Resumes, Educations


class CreateEducationView(LoginRequiredMixin, CreateView):
    template_name = 'educations/create_education.html'
    model = Educations
    form_class = EducationForm

    def post(self, request, pk, *args, **kwargs):
        form = self.form_class(request.POST)
        resume = get_object_or_404(Resumes, pk=pk)
        if form.is_valid():
            education = form.save(commit=False)
            education.save()
            resume.education.add(education)
            return redirect('resume', pk=pk)
        context = {}
        context['form'] = form
        return self.render_to_response(context)

    def get_success_url(self):
        return reverse('profile', kwargs={'pk': self.request.user.pk})


class EditEducationView(LoginRequiredMixin, UpdateView):
    template_name = 'educations/edit_education.html'
    model = Educations
    form_class = EducationForm

    def get_success_url(self):
        return reverse('resume', kwargs={'pk': self.kwargs.get('upk')})


class DeleteEducationView(LoginRequiredMixin, DeleteView):
    template_name = 'educations/delete_education.html'
    model = Educations
    context_object_name = 'education'

    def get(self, request, *args, **kwargs):
        self.resume_pk = kwargs.get('upk')
        return super(DeleteEducationView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        kwargs['resume_pk'] = self.resume_pk
        return super(DeleteEducationView, self).get_context_data(**kwargs)

    def get_success_url(self):
        return reverse('resume', kwargs={'pk': self.kwargs.get('upk')})
