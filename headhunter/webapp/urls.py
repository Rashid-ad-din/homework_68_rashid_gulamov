from django.urls import path

from webapp.views.educations import CreateEducationView, EditEducationView, DeleteEducationView
from webapp.views.experiences import CreateExperienceView, EditExperienceView, DeleteExperienceView
from webapp.views.index import IndexView
from webapp.views.resumes import CreateResumeView, ListResumesView, ResumeView, EditResumeView, DeleteResumeView
from webapp.views.vacancies import CreateVacancyView, ListVacancyView, VacancyView, EditVacancyView, DeleteVacancyView
from webapp.views.responds import RespondListView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('hh/', IndexView.as_view(), name='home'),

    path('hh/resume/create', CreateResumeView.as_view(), name='create_resume'),
    path('hh/resumes/<int:pk>', ListResumesView.as_view(), name='resumes'),
    path('hh/resume/<int:pk>', ResumeView.as_view(), name='resume'),
    path('hh/resume/<int:pk>/edit', EditResumeView.as_view(), name='edit_resume'),
    path('hh/resume/<int:pk>/delete', DeleteResumeView.as_view(), name='delete_resume'),

    path('hh/vacancy/create', CreateVacancyView.as_view(), name='create_vacancy'),
    path('hh/vacancies/<int:pk>', ListVacancyView.as_view(), name='vacancies'),
    path('hh/vacancy/<int:pk>/', VacancyView.as_view(), name='vacancy'),
    path('hh/vacancy/<int:pk>/edit', EditVacancyView.as_view(), name='edit_vacancy'),
    path('hh/vacancy/<int:pk>/delete', DeleteVacancyView.as_view(), name='delete_vacancy'),
    path('hh/respond/<int:pk>/', RespondListView.as_view(), name='responds'),

    path('hh/resume/<int:pk>/education/create/', CreateEducationView.as_view(), name='create_education'),
    path('hh/resume/<int:upk>/education/<int:pk>/edit/', EditEducationView.as_view(), name='edit_education'),
    path('hh/resume/<int:upk>/education/<int:pk>/delete', DeleteEducationView.as_view(), name='delete_education'),

    path('hh/resume/<int:pk>/experience/create/', CreateExperienceView.as_view(), name='create_experience'),
    path('hh/resume/<int:upk>/experience/<int:pk>/edit/', EditExperienceView.as_view(), name='edit_experience'),
    path('hh/resume/<int:upk>/experience/<int:pk>/delete', DeleteExperienceView.as_view(), name='delete_experience'),

]
