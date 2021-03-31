from django.shortcuts import render
from django.http import Http404
from django.views.generic import DetailView, UpdateView, CreateView, DeleteView
from django.views.generic.list import ListView
from .forms import *
from blog.models import *


def detail(request, id):
    try:
        p = CarOwner.objects.get(pk=id)
    except CarOwner.DoesNotExist:
        raise Http404("Owner does not exist")
    print(p)
    return render(request, 'Owner/detail.html', {'Owner': p})


def car_owners(request):

    context = {}

    context["dataset"] = CarOwner.objects.all()

    return render(request, "Owner/owner_list.html", context)


class CarOwnersList(ListView):
    # specify the model for list view
    model = CarOwner
    template_name = 'Owner/car_owner_ListView.html'


class CarList(ListView):
    # specify the model for list view
    model = Car
    template_name = 'Owner/car_list.html'


class ListCar(ListView):
    # specify the model for list view
    model = Car
    template_name = 'Owner/list_of_car.html'


class CarDetail(DetailView):
    model = Car
    template_name = 'Owner/CarDetail.html'


def create_car_owner(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    form = CarOwnerForm(
        request.POST or None)  # создание экземпляра формы, передача в него данных из формы (из полей в браузере)
    if form.is_valid():  # проверка формы на корректность (валидация)
        form.save()

    context['form'] = form

    return render(request, "Owner/create_car_owner.html", context)


class CarUpdate(UpdateView):
    model = Car
    fields = ['state_number', 'mark', 'model', 'color']
    # form_class = CarForm
    template_name = 'Owner/Update_Car.html'
    success_url = '/CarList/'


class CarCreate(CreateView):
    model = Car
    fields = ['state_number', 'mark', 'model', 'color']
    template_name = 'Owner/create_car_owner.html'
    success_url = '/CarList/'


class CarDelete(DeleteView):
    model = Car
    template_name = 'Owner/delete_car.html'
    success_url = '/CarList/'
