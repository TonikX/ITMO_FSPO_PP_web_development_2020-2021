# Create your views here.

from django.http import Http404
from django.shortcuts import render

from project_first_app.models import CarOwner

def detail(request, owner_id):
    try:
        p = CarOwner.objects.get(pk = owner_id)
    except CarOwner.DoesNotExist:
        raise Http404("Owner does not exist")
    return render(request, 'detail.html', {'owner': p})
