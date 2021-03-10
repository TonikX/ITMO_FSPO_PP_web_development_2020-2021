from django.http import Http404, HttpResponse

from django.shortcuts import \
    render  # импортирует метод, который "запускает" созданную хтмл страницу и передает в нее указанные параметры
from .models import *  # импортирует таблицу Poll из модели данных models, где polls - название приложения (и папки)
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


def detail(request):
    try:  # метод try-except - обработчик исключений
        p = CarOwner.objects.filter(pk__in=[1, 2, 3])
        print(p)
    except CarOwner.DoesNotExist:
        raise Http404(
            "Poll does not exist")  # исключение которое будет вызвано, если блок try вернет значение False (не будут найдены записи в таблице Poll)

    return render(request, 'blogfspo/detail.html', {
        'owner': p})


class list_car(ListView):
    model = Car
    template_name = 'blogfspo/detail_car.html'


class detail_car(DetailView):
    model = Car
    template_name = 'blogfspo/detail_car_o.html'
