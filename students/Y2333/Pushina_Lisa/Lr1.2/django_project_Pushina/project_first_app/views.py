from django.shortcuts import render
from django.http import Http404
from django.shortcuts import render

from .models import CarOwner


def detail(request, id_owner):
    try:
        c = CarOwner.objects.get(pk=id_owner)
    except CarOwner.DoesNotExist:
        raise Http404("CarOwner does not exist")

    return render(request, 'project_first_app/owner.html', {'owner': c})
