from django.http import Http404
from django.shortcuts import render
from project_first_app.models import CarOwner, Car
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .forms import OwnerForm
from django.views.generic.edit import *


def detail(request, car_owner_id):
    try:
        p = CarOwner.objects.get(pk=car_owner_id)
    except CarOwner.DoesNotExist:
        raise Http404("Owner does not exist")
    return render(request, 'owner.html', {'owner': p})


def list_owners(request):
    context = {"dataset": CarOwner.objects.all()}
    return render(request, "list_owners.html", context)


class CarList(ListView):
    model = Car
    template_name = 'list_car.html'


class CarListDetail(DetailView):
    model = Car
    template_name = 'car_detail.html'


def create_owner(request):
    context = {}

    # add the dictionary during initialization
    form = OwnerForm(
        request.POST or None)  # создание экземпляра формы, передача в него данных из формы (из полей в браузере)
    if form.is_valid():  # проверка формы на корректность (валидация)
        form.save()
    context['form'] = form
    return render(request, "create_owner.html", context)


class CarUpdate(UpdateView):
    model = Car
    fields = ['brand', 'model', 'color']
    template_name = 'car_form.html'
    success_url = '/cars/'


class CarCreate(CreateView):
    model = Car
    template_name = 'car_create_form.html'
    fields = ['state_number', 'brand', 'model', 'color']


class CarDelete(DeleteView):
    model = Car
    template_name = 'car_delete.html'
    success_url = '/cars/'
