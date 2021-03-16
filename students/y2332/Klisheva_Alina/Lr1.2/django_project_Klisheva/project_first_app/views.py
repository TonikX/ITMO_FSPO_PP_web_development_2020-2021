from django.shortcuts import render
from django.http import Http404
from .models import Car_owner


def detail(request, car_owner_id):
    try:
        owner = Car_owner.objects.get(pk=car_owner_id)
    except Car_owner.DoesNotExist:
        raise Http404("Owner does not exist")
    return render(request, 'owner.html', {'Owner': owner})
