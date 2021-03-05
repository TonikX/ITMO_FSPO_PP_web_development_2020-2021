from django.shortcuts import render
from django.http import Http404
from .models import CarOwner


def detail(request, owner_id):
    try:
        owner = CarOwner.objects.get(pk=owner_id)
    except CarOwner.DoesNotExist:
        raise Http404("Нет такого владельца")
    return render(request, 'owner.html', {"owner": owner})
