from django.http import Http404
from django.shortcuts import render
from project_first_app.models import CarOwner

def detail(request, id_owner):
    try:
        p = CarOwner.objects.get(pk=id_owner)
    except CarOwner.DoesNotExist:
        raise Http404("Car owner does not exist")
    return render(request, 'owner.html', {'owner': p})
