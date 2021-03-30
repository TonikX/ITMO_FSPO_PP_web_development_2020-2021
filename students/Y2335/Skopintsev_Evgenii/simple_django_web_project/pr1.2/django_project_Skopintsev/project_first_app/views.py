from django.http import Http404
from django.shortcuts import render
from project_first_app.models import CarOwner


def detail(request, car_owner_id):
    try:
        p = CarOwner.objects.get(pk=car_owner_id)
    except CarOwner.DoesNotExist:
        raise Http404("Car does not exist")
    return render(request, 'owner.html', {'owner': p})
