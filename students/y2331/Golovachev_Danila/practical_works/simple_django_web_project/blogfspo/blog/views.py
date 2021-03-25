from django.http import Http404, HttpResponse

from django.shortcuts import \
    render  # импортирует метод, который "запускает" созданную хтмл страницу и передает в нее указанные параметры
from .models import *  # импортирует таблицу Poll из модели данных models, где polls - название приложения (и папки)
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import CreateView
from .forms import *


def detail(request):
    try:  # метод try-except - обработчик исключений
        p = CarOwner.objects.filter(pk__in=[1, 2, 3, 4, 5, 6])
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


def create_view(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    form = CreateForm(
        request.POST or None)  # создание экземпляра формы, передача в него данных из формы (из полей в браузере)
    if form.is_valid():  # проверка формы на корректность (валидация)
        form.save()
    context['form'] = form

    return render(request, "blogfspo/create_view.html", context)


class CarUpdateView(UpdateView):
    model = Car
    fields = ['mark', 'model', 'color', 'number']
    template_name = 'blogfspo/car_form.html'
    success_url = '/Cars/'


class CarDeleteView(DeleteView):
    model = Car
    template_name = 'blogfspo/delete_car.html'
    success_url = '/Cars/'


class CarCreateView(CreateView):
    model = Car
    fields = ['mark', 'model', 'color', 'number']
    template_name = 'blogfspo/car_create.html'
    success_url = '/Cars/'
