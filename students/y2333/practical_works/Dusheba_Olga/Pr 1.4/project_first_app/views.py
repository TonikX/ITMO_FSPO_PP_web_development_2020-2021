from django.http import Http404
from django.shortcuts import render
from django.views.generic import UpdateView, DeleteView, CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import CarOwner
from .models import Car


def detail(request, owner_id):
    try:
        p = CarOwner.objects.get(pk=owner_id)
    except CarOwner.DoesNotExist:
        raise Http404("Car owner does not exist")
    return render(request, 'detail.html', {'owner': p})


def list_view(request):
    # словарь для исходных данных
    # имена полей как ключи
    context = {}
    # добавление данных об объектах, полученных в результате выполнения запроса exampleModel.objects.all() в словарь
    context["dataset"] = Car.objects.all()
    return render(request, "list_view.html", context)


class CarList(ListView):
    model = Car
    template_name = 'car_list_view.html'


class OwnerList(ListView):
    model = CarOwner
    template_name = 'owner_list_view.html'


class CarView(DetailView):
    model = Car


class OwnerView(DetailView):
    model = CarOwner


class CarUpdateView(UpdateView):
    model = Car
    fields = [
        "gos_number",
        "mark",
        "model",
        "color",
    ]
    success_url = '/car_list_view/'


class CarDeleteView(DeleteView):
    model = Car
    success_url = "/car_list_view/"


class CarCreateView(CreateView):
    model = Car
    fields = [
        "gos_number",
        "mark",
        "model",
        "color",
    ]
    success_url = '/car_list_view/'


class OwnerUpdateView(UpdateView):
    model = CarOwner
    fields = [
        "username",
        "last_name",
        "first_name",
        "birth_date",
        "passport_number",
        "home_address",
        "nationality",
    ]
    success_url = '/owner_list_view/'


class OwnerDeleteView(DeleteView):
    model = CarOwner
    success_url = "/owner_list_view/"


class OwnerCreateView(CreateView):
    model = CarOwner
    fields = [
        "username",
        "last_name",
        "first_name",
        "birth_date",
        "birth_date",
        "passport_number",
        "home_address",
        "nationality",
    ]
    success_url = '/owner_list_view/'
