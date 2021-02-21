from django.shortcuts import render
from django.http import Http404
from .models import CarOwner


def detail(request, car_owner_id):
    try:
        owner = CarOwner.objects.get(pk=car_owner_id)
    except:
        raise Http404("Car owner does not exist")

    return render(request, 'owner.html', {'owner': owner})
