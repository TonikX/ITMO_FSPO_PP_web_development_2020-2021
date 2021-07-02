from django.http import Http404
from django.shortcuts import render
from project_first_app.models import CarOwner


# Create your views here.
def detail(request, owner_id):
    try:
        owner = CarOwner.objects.get(pk=owner_id)
    except CarOwner.DoesNotExist:
        raise Http404("CarOwner does not exist")
    return render(request, 'owner.html', {'owner': owner})
