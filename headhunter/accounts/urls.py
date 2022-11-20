from django.urls import path

from accounts.views import LoginView, logout_view, RegisterView, ProfileView, UserChangeView, PasswordChangeView
from webapp.views.resumes import CreateResumeView, ListResumesView, ResumeView, EditResumeView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('profile/<int:pk>/password-change/', PasswordChangeView.as_view(), name='password_change'),
    path('profile/<int:pk>/change/', UserChangeView.as_view(), name='change'),
    path('profile/<int:pk>/resumes/create', CreateResumeView.as_view(), name='create_resume'),
    path('profile/<int:pk>/resumes/', ListResumesView.as_view(), name='resumes'),
    path('profile/<int:upk>/resume/<int:pk>/', ResumeView.as_view(), name='resume'),
    path('profile/<int:upk>/resume/<int:pk>/edit', EditResumeView.as_view(), name='edit_resume'),
]
