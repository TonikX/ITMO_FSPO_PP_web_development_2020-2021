from django.http import Http404
from django.shortcuts import render
from .models import *
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .forms import Owner_form  # импортируем только-что созданную форму
from django.views.generic.edit import UpdateView
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView


def detail(request, owner_id):
    try:  # метод try-except - обработчик исключений
        o = Owner.objects.get(pk=owner_id)
    except Owner.DoesNotExist:
        raise Http404("Owner does not exist")
        # исключение которое будет вызвано, если блок try вернет значение False (не будут найдены записи в таблице Poll)
    return render(request, 'first/owner.html', {'owner': o})
    # данная строка рендерит хтмл страницу detail.html и передает в него объект "p", который в хтмл шаблоне будет
    # называться "poll"


def owners(request):
    # dictionary for initial data with
    # field names as keys
    context = {"owner_list": Owner.objects.all()}

    # add the dictionary during initialization [en]
    # добавление данных об объектах, полученных в результате выполнения запроса exampleModel.objects.all() в словарь

    return render(request, "first/owners.html", context)


class car_list(ListView):
    # specify the model for list view
    model = Car
    template_name = 'first/car_list.html'


class car(DetailView):
    model = Car
    template_name = 'first/car_view.html'


class cars(ListView):
    model = Car
    queryset = model.objects.all()

    def get_queryset(self):
        owner_id = self.request.GET.get('owner_id')

        if owner_id:

            try:
                owner_id = int(owner_id)
                queryset = self.queryset.filter(owner_id=owner_id)

            except ValueError:
                queryset = self.model.objects.none()

            return queryset

        return self.queryset

    template_name = 'first/cars.html'


def create_view(request):
    # dictionary for initial data with
    # field names as keys
    context = {}
    # add the dictionary during initialization
    form = Owner_form(request.POST or None)
    # создание экземпляра формы, передача в него данных из формы (из полей в браузере)
    if form.is_valid():  # проверка формы на корректность (валидация)
        form.save()
    context['form'] = form
    return render(request, "first/create_owner.html", context)


class Car_update(UpdateView):
    model = Car
    fields = ["gov_number", "brand", "model", "colour"]
    success_url = '/cars/'
    template_name = 'first/update_car.html'


class Car_create(CreateView):
    # specify the model for create view
    model = Car
    template_name = 'first/create_car.html'

    # specify the fields to be displayed

    fields = ['car_id', 'gov_number', 'brand', 'model', 'colour']


class Car_delete(DeleteView):
    model = Car
    success_url = '/cars/'
    template_name = 'first/delete_car.html'
