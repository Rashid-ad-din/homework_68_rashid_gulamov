from django.contrib import admin
from django.urls import path

from webapp.views.index import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index')
]
