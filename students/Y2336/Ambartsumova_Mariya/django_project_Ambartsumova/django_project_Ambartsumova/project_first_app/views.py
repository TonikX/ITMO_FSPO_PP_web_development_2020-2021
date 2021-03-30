from django.http import Http404
from django.shortcuts import render
from project_first_app.models import CarOwner


def detail(request, id):
    try:
        p = CarOwner.objects.get(pk=id)
    except CarOwner.DoesNotExist:
        raise Http404("Owner does not exist")
    return render(request, 'templates/owner.html', {'CarOwner': p})
