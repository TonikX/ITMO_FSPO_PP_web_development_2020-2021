from django.shortcuts import render
from django.http import Http404
from .models import car_owner

def detail(request, id):
    try:
        p = car_owner.objects.get(pk=id)
    except car_owner.DoesNotExist:
        raise Http404("car owner does not exist")
    return render(request, 'car_owner.html', {'car_owner': p})