from django.shortcuts import render

from django.http import Http404
from django.shortcuts import render
from blog.models import CarOwner
def detail(request, owner_id):
    try:
        owner = CarOwner.objects.get(pk=owner_id)
    except CarOwner.DoesNotExist:
        raise Http404("CarOwner does not exist")
    return render(request, 'index.html', {'CarOwner': owner})

