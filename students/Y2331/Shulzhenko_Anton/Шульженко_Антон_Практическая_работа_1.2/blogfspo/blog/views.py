from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render
from blog.models import carOwner


def detail(request, carOwner_id):
    try:
        p = carOwner.objects.get(pk=carOwner_id)
    except carOwner.DoesNotExist:
        raise Http404("Poll does not exist")
    return render(request, 'blog/post_list.html', {'carOwner': p})


def startPage(request):
    html = "<h2>Добро пожаловать на стартовую страницу Шульженко Антона!</h2></br>"
    html += '<a href="http://127.0.0.1:8000/carOwner/1">About first car owner</a></br>'
    html += '<a href="http://127.0.0.1:8000/carOwner/2">About second car owner</a>'
    html += '<h3><a href="http://127.0.0.1:8000/admin">Панель администратора</a></h3>'
    return HttpResponse(html)

