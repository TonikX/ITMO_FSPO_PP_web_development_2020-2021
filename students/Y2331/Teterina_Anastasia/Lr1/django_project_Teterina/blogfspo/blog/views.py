from django.shortcuts import render

from django.http import Http404
# импортирует метод обработки ситуации, когда нет    необходимых записей в бд (обработчик ошибок)
from django.shortcuts import \
    render  # импортирует метод, который "запускает" созданную хтмл страницу и передает в нее указанные параметры
from blog.models import *
# импортирует таблицу Poll из модели данных models, где polls - название приложения (и папки)
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .forms import *
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import UpdateView


def detail(request):
    try:  # метод try-except - обработчик исключений
        o = Owner.objects.filter(
            pk__in=[1, 2, 3, 4,
                    5])  # pk - автоматически создается в джанго для любой таблицы в моделе (оно есть у любого объекта из бд), poll_id будет передан функции при её вызове.
    # переменной p присваивается объект, полученный в результате выполнения запроса аналогичного "select * from Poll where pk=poll_id"
    except Owner.DoesNotExist:
        raise Http404(
            "Owner does not exist")  # исключение которое будет вызвано, если блок try вернет значение False (не будут найдены записи в таблице Poll)
    return render(request, 'first/owner.html', {
        'owner': o})  # данная строка рендерит хтмл страницу detail.html и передает в него объект "p", который в хтмл шаблоне будет называться "poll"


def create_view(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    form = ExampleForm(
        request.POST or None)  # создание экземпляра формы, передача в него данных из формы (из полей в браузере)
    if form.is_valid():  # проверка формы на корректность (валидация)
        form.save()
    context['form'] = form
    return render(request, "first/create_view.html", context)


class list_car(ListView):
    model = Car
    template_name = 'first/list_car.html'


class detail_car(DetailView):
    model = Car
    template_name = 'first/id_car.html'


class Car_create(CreateView):
    model = Car
    fields = ["car_id", "gov_number", "brand", "model", "colour"]
    template_name = 'first/create_car.html'


class Car_delete(DeleteView):
    model = Car
    fields = ["car_id", "gov_number", "brand", "model", "colour"]
    template_name = 'first/delete_car.html'


class Car_update(UpdateView):
    model = Car
    fields = ["car_id", "gov_number", "brand", "model", "colour"]
    template_name = 'first/update_car.html'

