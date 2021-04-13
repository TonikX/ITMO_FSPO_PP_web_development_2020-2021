from blog.models import Publisher  # импорт данных из таблиц
from django.http import HttpResponse
import datetime
from .models import ExampleModel
from django.views.generic.detail import DetailView
from django.http import Http404
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from .forms import Owner_f
from .forms import Car, Car_f
from django.views.generic.edit import DeleteView
from .models import Owner
from django.shortcuts import render




def detail(request, owner_id):  # что импортирует
    try:
        o = Owner.objects.get(pk=owner_id)  # овнер - таблица, get импорт, овнер_айди - что импортировать
    except Owner.DoesNotExist:  # если отсутствие
        raise Http404("Owner does not exist")  # что выведет, если нет данных в таблице
        return render(request, 'first/owner.html', {'owner': o})  # шаблон хтмл страницы, в который передается o = овнер


# create a function
def example_view(request):
    # получение даты и времени
    now = datetime.datetime.now()
    # конвертирование в сротку
    html = "Time is {}".format(now)
    # вывод ответа
    return HttpResponse(html)


# relative import of forms


def list_view(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization [en]
    # добавление данных об объектах, полученных в результате выполнения запроса exampleModel.objects.all() в словарь
    context["dataset"] = ExampleModel.objects.all()
    # Вывод хтмл шаблона с добавленными данными
    return render(request, "second/list_view.html", context)


class ExampleList(ListView):
    # Выбор модели, которая будет выводиться списком
    model = ExampleModel
    # указали модель качестве родительского и переопределили значение атрибута
    template_name = 'third/cvb_list_view.html'


# Создание класса, в котором будет отображаться простое представление Publisher
class PublisherRetrieveView(DetailView):
    model = Publisher


# обработка ошибок(если данных нет в бд)


def detail(request, last_name):  # что импортирует
    try:
        o = Owner.objects.get(pk=last_name)  # овнер - таблица, get импорт, ласт нейм - что импортировать
    except Owner.DoesNotExist:  # если отсутствие
        raise Http404("Owner does not exist")  # что выведет, если нет данных в таблице
    return render(request, '5/Owner_2.html', {'Owner': o})  # шаблон хтмл страницы, в который передается o = овнер


# Практическое задание №1



# Практика №2
class CarListView(ListView):  # ListView - отображение списка и страницы подробной информации для одиночного объекта.
    model = Car  # Указываем, какую модель будем использовать
    queryset = model.objects.all()  # QuerySet – это итератор, и при первом выполнении итерации будет произведен запрос к базе данных. Следовательно, происходит запрос к БД на вывод всех полей
    template_name = '7/cars.html'  # указываем, где хранится шаблон для данного listview

    def get_queryset(
            self):  # Функция get_queryset() переопределяет получение queryset, обращаясь к GET-параметрам из запроса. В случае, если параметр owner определен и является числом, происходит фильтрация и функция возвращает отфильтрованные данные.
        owner = self.request.GET.get('owner')  # обращение к get-параметрам

        if owner:  # если овнер == 1

            try:
                owner = int(owner)  # если гет- параметр от вызова овнера является чилом то
                queryset = self.queryset.filter(owner=owner)  # происходит фильтрация и вывод отфильтрованных данных

            except ValueError:
                queryset = self.model.objects.none()

            return queryset

        return self.queryset

    # Практика 3


def create_view(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    form = Owner_f(
        request.POST or None)  # создание экземпляра формы, передача в него данных из формы (из полей в браузере)
    if form.is_valid():  # проверка формы на корректность (валидация)
        form.save()  # сохранение формы
    context['form'] = form  # заполням массив данными из форм
    return render(request, "8/create_view.html", context)  # вывод формы


def create_view(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    form = Car_f(
        request.POST or None)  # создание экземпляра формы, передача в него данных из формы (из полей в браузере)
    if form.is_valid():  # проверка формы на корректность (валидация)
        form.save()
    context['form'] = form  # заполням массив данными из форм
    return render(request, "9/create_view_car.html", context)  # вывод формы


class CarUpdateView(
    UpdateView):  # Представление, которое отображает форму для редактирования существующего объекта, повторного отображения формы с ошибками проверки (если они есть) и сохранения изменений в объекте.
    model = Car  # модель, которую будем использовать
    fields = ['Brand', 'State_number', 'Model', 'Color']  # поля, которые будем использовать
    success_url = '/7/cars/list/'  # ссылка для вывода всех машин
    template_name = '10/car_form.html'  # место, где хранится шаблон


class CarDeleteView(DeleteView):  # представление для удаления полей
    model = Car  # модель, которую будем использовать
    success_url = '/car/list/'  # ссылка для вывода всех машин
    template_name = '11/car_form_2.html'  # хтмл шаблон


class Owner(ListView):  # ListView - отображение списка и страницы подробной информации для одиночного объекта.
    # Указываем, какую модель будем использовать
    model = Owner
    template_name = '12/owner_list.html'  # указываем, где хранится шаблон для данного listview
