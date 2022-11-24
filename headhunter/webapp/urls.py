from django.urls import path

from webapp.views.educations import CreateEducationView, EditEducationView, DeleteEducationView
from webapp.views.experiences import CreateExperienceView, EditExperienceView, DeleteExperienceView
from webapp.views.index import IndexView
from webapp.views.respond_messages import AddRespondMessageView, DeleteRespondMessageView
from webapp.views.resumes import CreateResumeView, ListResumesView, ResumeView, EditResumeView, DeleteResumeView
from webapp.views.vacancies import CreateVacancyView, ListVacancyView, VacancyView, EditVacancyView, DeleteVacancyView
from webapp.views.responds import RespondListView, RespondView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('hh/', IndexView.as_view(), name='home'),

    path('hh/user/<int:pk>/resumes/create/', CreateResumeView.as_view(), name='create_resume'),
    path('hh/user/<int:pk>/resumes/', ListResumesView.as_view(), name='resumes'),
    path('hh/user/<int:upk>/resumes/<int:pk>/', ResumeView.as_view(), name='resume'),
    path('hh/user/<int:upk>/resumes/<int:pk>/edit/', EditResumeView.as_view(), name='edit_resume'),
    path('hh/user/<int:upk>/resumes/<int:pk>/delete/', DeleteResumeView.as_view(), name='delete_resume'),

    path('hh/user/<int:upk>/vacancy/create/', CreateVacancyView.as_view(), name='create_vacancy'),
    path('hh/user/<int:pk>/vacancies/', ListVacancyView.as_view(), name='vacancies'),
    path('hh/user/<int:upk>/vacancies/<int:pk>/', VacancyView.as_view(), name='vacancy'),
    path('hh/user/<int:upk>/vacancies/<int:pk>/edit/', EditVacancyView.as_view(), name='edit_vacancy'),
    path('hh/user/<int:upk>/vacancies/<int:pk>/delete/', DeleteVacancyView.as_view(), name='delete_vacancy'),

    path('hh/user/<int:pk>/responds/', RespondListView.as_view(), name='responds'),
    path('hh/user/<int:upk>/resumes/<int:rpk>/respond/<int:pk>/', RespondView.as_view(), name='respond'),
    path('hh/user/<int:upk>/resumes/<int:rpk>/respond/<int:pk>/add-message/',
         AddRespondMessageView.as_view(),
         name='add_respond_message'),
    path('hh/user/<int:upk>/responds/<int:rpk>/respond-message/<int:pk>/delete/',
         DeleteRespondMessageView.as_view(),
         name='delete_respond_message'),

    path('hh/user/<int:upk>/resumes/<int:pk>/educations/create/', CreateEducationView.as_view(),
         name='create_education'),
    path('hh/user/<int:upk>/resumes/<int:rpk>/educations/<int:pk>/edit/', EditEducationView.as_view(),
         name='edit_education'),
    path('hh/user/<int:upk>/resumes/<int:rpk>/educations/<int:pk>/delete/', DeleteEducationView.as_view(),
         name='delete_education'),

    path('hh/user/<int:upk>/resumes/<int:pk>/experiences/create/', CreateExperienceView.as_view(),
         name='create_experience'),
    path('hh/user/<int:upk>/resumes/<int:rpk>/experiences/<int:pk>/edit/', EditExperienceView.as_view(),
         name='edit_experience'),
    path('hh/user/<int:upk>/resume/<int:rpk>/experiences/<int:pk>/delete/', DeleteExperienceView.as_view(),
         name='delete_experience'),

]
