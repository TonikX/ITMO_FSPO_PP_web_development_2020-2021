from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render
from project_first_app.models import owner
import datetime

def mainpage(request):
    now = datetime.datetime.now()
    html = "<html><body><p><strong>Hello world!</strong></p><pЭтот сайт создал студент группы Y2335 Ягнаев Владимир</p><p>Сейчас %s.</p></body></html>" % now
    return HttpResponse(html)

def detail(request, poll_id):
    try:
        p = owner.objects.get(pk=poll_id)
    except owner.DoesNotExist:
        raise Http404("Owner does not exist")
    return render(request, 'templates/owner.html', {'owner': p})