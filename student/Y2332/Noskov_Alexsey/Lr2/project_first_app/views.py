from django.http import Http404
from django.shortcuts import render
from .models import CarOwner

def detail(request, owner_id):
    try:
        p = CarOwner.objects.get(pk=owner_id)
    except CarOwner.DoesNotExist:
        raise Http404("CarOwner does not exist")
    return render(request, 'owner.html', {'owner': p})
# Create your views here.
