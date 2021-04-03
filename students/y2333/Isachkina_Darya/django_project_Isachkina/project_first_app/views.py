from django.http import Http404
from django.shortcuts import render
from project_first_app.models import *
from project_first_app.forms import *
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import CreateView


def detail(request, owner_id):
    try:
        p = CarOwner.objects.get(pk=owner_id)
    except CarOwner.DoesNotExist:
        raise Http404("CarOwner does not exist")
    return render(request, 'owner.html', {'owner': p})


def car(request):
    return Http404("car")

# Вывод владельцев функционально
def owner_list(request):
    сar_owner = {}
    сar_owner["dataset"] = CarOwner.objects.all()
    return render(request, "owner_list.html", сar_owner)


# Вывод всех владельцев на основе класса
class Car_list(ListView):
    model = Car
    template_name = 'class_car_list.html'


# Вывод владельца автомобиля по id
class CarOwner_id(DetailView):
    model = CarOwner


# Вывод автомобиля по id
class Car_id(DetailView):
    model = Car


class CarList(ListView):
    model = Car
    queryset = model.objects.all()

    def get_queryset(self):
        car_id = self.request.GET.get('сar_id')
        if car_id:
            try:
                car_id = int(car_id)
                queryset = self.queryset.filter(car_id=car_id)
            except ValueError:
                queryset = self.model.objects.none()
            return queryset
        return self.queryset


def create_owner(request):
    context = {}

    form = OwnerForm(request.POST or None) # создание экземпляра формы, передача в него данных из формы (из полей в браузере)
    if form.is_valid(): # проверка формы на корректность (валидация)
        form.save()
    context['form'] = form
    return render(request, "create_owner.html", context)


class CarUpdate(UpdateView):
    model = Car
    fields = ['gos_number', 'mark', 'model', 'color']
    success_url = '/car/list/'


class CarCreate(CreateView):
    model = Car
    fields = ['gos_number', 'mark', 'model', 'color']
    success_url = '/car/list/'


class CarDelete(DeleteView):
    model = Car
    success_url = '/car/list/'