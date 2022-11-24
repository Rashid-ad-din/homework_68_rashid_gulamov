from django.views.generic import ListView, DetailView

from webapp.forms.responds import RespondMessageForm
from webapp.models import Respond


class RespondListView(ListView):
    template_name = 'responds/responds_list.html'
    model = Respond
    context_object_name = 'responds'


class RespondView(DetailView):
    template_name = 'responds/respond.html'
    model = Respond
    context_object_name = 'respond'

    def get(self, request, *args, **kwargs):
        self.extra_context = {'message_form': RespondMessageForm()}
        return super().get(request, *args, **kwargs)
