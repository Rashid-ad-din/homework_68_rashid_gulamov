from django.contrib import admin

from webapp.models import Vacancies
from webapp.models import Resumes

# Register your models here.
admin.site.register(Vacancies)
admin.site.register(Resumes)
