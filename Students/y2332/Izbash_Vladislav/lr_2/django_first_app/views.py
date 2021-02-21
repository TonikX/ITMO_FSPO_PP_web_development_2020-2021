from django.shortcuts import render
from django.http import Http404

from django_first_app.models import CarOwner


def get_owner(request, owner_id):
    try:
        owner = CarOwner.objects.get(pk=owner_id)
    except CarOwner.DoesNotExist:
        raise Http404("Car owner does not exist")

    return render(request, 'owner.html', {'owner': owner})
