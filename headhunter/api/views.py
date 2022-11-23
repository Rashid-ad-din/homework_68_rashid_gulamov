from django.http import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt
from rest_framework.response import Response
from rest_framework.views import APIView
from webapp.models import Respond, Vacancies, Resumes


class AddResumeView(APIView):
    def post(self, request, *args, **kwargs):
        vacancy = get_object_or_404(Vacancies, pk=request.data.get('vacancy', False))
        resume = get_object_or_404(Resumes, pk=request.data.get('resume', False))
        for respond in Respond.objects.all():
            print(respond.resume.pk)
            # print(int(request.data['resume']))
            if respond.resume.pk == int(request.data.get('resume', False)) and \
                    respond.vacancy.pk == int(request.data.get('vacancy', False)):
                print('hui')
                return Response({'error': 'Вы уже откликнулись'}, status=400)
        Respond.objects.create(vacancy=vacancy, resume=resume)
        return Response({'answer': 'Отклик отправлен'})


@ensure_csrf_cookie
def get_token_view(request, *args, **kwargs):
    if request.method == 'GET':
        return HttpResponse()
    return HttpResponseNotAllowed('Only GET request are allowed')
