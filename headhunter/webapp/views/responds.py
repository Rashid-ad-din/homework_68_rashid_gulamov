from django.views.generic import ListView
from webapp.models import Respond


class RespondListView(ListView):
    template_name = 'responds/responds_list.html'
    model = Respond
    context_object_name = 'responds'
