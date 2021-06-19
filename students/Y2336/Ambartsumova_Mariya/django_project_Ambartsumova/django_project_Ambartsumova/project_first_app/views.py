from django.http import Http404
from django.shortcuts import render
from project_first_app.models import CarOwner, Car
from .forms import CarOwnerForm
from .forms import CarForm
from django.views.generic.edit import UpdateView, DeleteView


class CarDeleteView(DeleteView):
    model = Car
    success_url = '/listCars/'


class CarOwnerDeleteView(DeleteView):
    model = CarOwner
    success_url = '/listOwners/'


class CarUpdateView(UpdateView):
    model = Car
    fields = ['state_number', 'brand', 'model', 'color']
    success_url = '/listCars'
    template_name = ''


class CarOwnerUpdateView(UpdateView):
    model = CarOwner
    fields = ['first_name', 'second_name', 'birth_date']

    success_url = '/listOwners'


def listOwners(request):
    context = {}
    context["dataset"] = CarOwner.objects.all()

    return render(request, "../templates/project_first_app/listOwners.html", context)


def owner(request, id):
    try:
        p = CarOwner.objects.get(pk=id)
    except CarOwner.DoesNotExist:
        raise Http404("Owner does not exist")
    return render(request, "templates/owner.html", {"CarOwner": p})


def listCars(request):
    context = {}
    context["dataset"] = Car.objects.all()

    return render(request, "templates/listCars.html", context)


def car(request, id):
    try:
        p = Car.objects.get(pk=id)
    except Car.DoesNotExist:
        raise Http404("Car does not exist")
    return render(request, "templates/car.html", {"Car": p})


def create_owner(request):
    context = {}

    form = CarOwnerForm(
        request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "templates/createOwner.html", context)


def create_car(request):
    context = {}

    form = CarForm(
        request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "templates/project_first_app/createCar.html", context)
