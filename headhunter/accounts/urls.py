from django.urls import path

from accounts.views import LoginView, LogoutView, RegisterView, ProfileView, UserChangeView, PasswordChangeView
from webapp.views.resumes import CreateResumeView, ListResumesView, ResumeView, EditResumeView
from webapp.views.vacancies import CreateVacancyView, ListVacancyView, VacancyView, EditVacancyView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('profile/<int:pk>/password-change/', PasswordChangeView.as_view(), name='password_change'),
    path('profile/<int:pk>/change/', UserChangeView.as_view(), name='change'),
    path('profile/<int:pk>/resumes/create', CreateResumeView.as_view(), name='create_resume'),
    path('profile/<int:pk>/resumes/', ListResumesView.as_view(), name='resumes'),
    path('profile/<int:upk>/resume/<int:pk>/', ResumeView.as_view(), name='resume'),
    path('profile/<int:upk>/resume/<int:pk>/edit', EditResumeView.as_view(), name='edit_resume'),
    path('profile/<int:pk>/vacancies/create', CreateVacancyView.as_view(), name='create_vacancy'),
    path('profile/<int:pk>/vacancies/', ListVacancyView.as_view(), name='vacancies'),
    path('profile/<int:upk>/vacancies/<int:pk>/', VacancyView.as_view(), name='vacancy'),
    path('profile/<int:upk>/vacancies/<int:pk>/edit', EditVacancyView.as_view(), name='edit_vacancy'),
]
