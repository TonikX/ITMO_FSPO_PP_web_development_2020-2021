from django.shortcuts import render
from django.http import Http404
from django.shortcuts import render
from .models import Car
from .models import CarOwner
from .models import Own
from .models import Doc


def detail(request, owner_id):
    try:
        p = CarOwner.objects.get(pk=owner_id)
    except Car.DoesNotExist:
        raise Http404("CarOwner does not exist")
    return render(request, 'owner.html', {'owner': p})
