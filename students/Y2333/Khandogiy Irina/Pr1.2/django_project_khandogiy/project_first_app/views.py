from django.http import Http404

from django.shortcuts import render

from project_first_app.models import CarOwner


def detail(request, owner_id):
    try:
        c = CarOwner.objects.get(pk=owner_id)
    except CarOwner.DoesNotExist:
        raise Http404("CarOwner does not exist")
    return render(request, "first_app/owner.html", {'owner': c})
