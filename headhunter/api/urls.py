from django.urls import path
from api.views import AddResumeView, get_token_view, EditAccountView

urlpatterns = [
    path('token/', get_token_view, name='token'),
    path('add_resume/', AddResumeView.as_view(), name='add_resume'),
    path('edit_account/', EditAccountView.as_view(), name='edit_account'),
]
