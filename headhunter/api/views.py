from django.http import HttpResponse, HttpResponseNotAllowed, JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework.response import Response
from rest_framework.views import APIView
from webapp.models import Respond, Vacancies, Resumes
from accounts.models import Account


class AddResumeView(APIView):
    def post(self, request, *args, **kwargs):
        vacancy = get_object_or_404(Vacancies, pk=request.data.get('vacancy', False))
        resume = get_object_or_404(Resumes, pk=request.data.get('resume', False))
        for respond in Respond.objects.all():
            if respond.resume.pk == int(request.data.get('resume', False)) and \
                    respond.vacancy.pk == int(request.data.get('vacancy', False)):
                return Response({'error': 'Вы уже откликнулись'}, status=400)
        Respond.objects.create(vacancy=vacancy, resume=resume)
        return Response({'answer': 'Отклик отправлен'})


class EditAccountView(APIView):
    def post(self, request, *args, **kwargs):
        if request.data.get('username', False) == '':
            return JsonResponse({'error': 'Поле логина пустое'}, status=400)
        if request.data.get('name', False) == '':
            return JsonResponse({'error': 'Поле имени пустое'}, status=400)
        if request.data.get('lastname', False) == '':
            return JsonResponse({'error': 'Поле фамилии пустое'}, status=400)
        if request.data.get('email', False) == '':
            return JsonResponse({'error': 'Поле почты пустое'}, status=400)
        if request.data.get('phone', False) == '':
            return JsonResponse({'error': 'Поле номера пустое'}, status=400)
        for account in Account.objects.all():
            if self.request.user.username == request.data.get('username', False):
                pass
            elif account.username == request.data.get('username', False):
                return JsonResponse({'error': 'Такое имя уже есть'}, status=400)
            if self.request.user.email == request.data.get('email', False):
                pass
            elif account.email == request.data.get('email', False):
                return JsonResponse({'error': 'Такая почта уже есть'}, status=400)
        Account.objects.filter(pk=self.request.user.pk).update(username=request.data.get('username', False),
                                                               email=request.data.get('email', False),
                                                               first_name=request.data.get('name', False),
                                                               last_name=request.data.get('lastname', False),
                                                               phone=request.data.get('phone', False),
                                                               avatar=request.data.get('avatar', False)
                                                               )
        print(Account.objects.filter(pk=self.request.user.pk))
        return JsonResponse({'answer': 'Данные успешно обновлены'})


@ensure_csrf_cookie
def get_token_view(request, *args, **kwargs):
    if request.method == 'GET':
        return HttpResponse()
    return HttpResponseNotAllowed('Only GET request are allowed')
