from django.http import Http404
from django.shortcuts import render
from project_first_app.models import CarOwner, Car
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


def detail(request, car_owner_id):
    try:
        p = CarOwner.objects.get(pk=car_owner_id)
    except CarOwner.DoesNotExist:
        raise Http404("Car does not exist")
    return render(request, 'owner.html', {'owner': p})


def list_owners(request):
    context = {"dataset": CarOwner.objects.all()}
    return render(request, "list_owners.html", context)


class CarList(ListView):
    model = Car
    template_name = 'list_car.html'


class CarListDetail(DetailView):
    model = Car
