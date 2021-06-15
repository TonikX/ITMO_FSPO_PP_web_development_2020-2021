from django.http import Http404
from django.shortcuts import render
from blog.models import CarOwner
from blog.models import DrivingLicense


def detail(request, ID_owner):
    try:
        c = CarOwner.objects.get(pk=ID_owner)
    except CarOwner.DoesNotExist:
        raise Http404("CarOwner does not exist")
    return render(request, "owner.html", {'owner': c})

