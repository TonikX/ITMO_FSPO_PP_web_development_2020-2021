from django.http import Http404
from django.shortcuts import render
from .models import CarOwner
from .models import Car
def detail_owner(request, CarOwner_id):
    try:
        p = CarOwner.objects.get(pk=CarOwner_id)
    except CarOwner.DoesNotExist:
        raise Http404("Owner does not exist")
    return render(request, 'project_first_app/CarOwner_detail.html', {'CarOwner': p})

def detail_car(request, Car_id):
    try:
        p = Car.objects.get(pk=Car_id)
    except Car.DoesNotExist:
        raise Http404("Car does not exist")
    return render(request, 'project_first_app/car_detail.html', {'Car': p})