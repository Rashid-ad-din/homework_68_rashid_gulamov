from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import CreateView, DeleteView

from accounts.models import Account
from webapp.forms.responds import RespondMessageForm
from webapp.models import Respond, RespondMessage


class AddRespondMessageView(CreateView):
    model = RespondMessage
    form_class = RespondMessageForm
    template_name = 'responds/respond.html'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        user_pk = kwargs.get('upk')
        respond_pk = kwargs.get('pk')
        if form.is_valid():
            respond_message = form.save(commit=False)
            respond_message.respond = get_object_or_404(Respond, pk=respond_pk)
            respond_message.author = get_object_or_404(Account, pk=user_pk)
            respond_message.save()
            return redirect('respond', user_pk, respond_pk)
        return redirect('respond', user_pk, respond_pk)


class DeleteRespondMessageView(DeleteView):
    template_name = 'responds/delete_message.html'
    model = RespondMessage
    context_object_name = 'respond_message'

    def get_success_url(self):
        return reverse('respond', kwargs={'upk': self.request.user.pk, 'pk': self.object.respond.pk})
