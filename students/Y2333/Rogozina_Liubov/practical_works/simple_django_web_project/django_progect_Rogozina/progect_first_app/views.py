from django.shortcuts import render

# Create your views here
from django.http import Http404
from progect_first_app.models import Car_owner
from progect_first_app.models import Car
from progect_first_app.models import Ownership
from progect_first_app.models import Driver_license
def owner(request, carowner_id):
    try:
        o = Car_owner.objects.get(pk=carowner_id)

    except Car_owner.doesNotExists:
        raise Http404("Car owner does not exists")
    return render(request, 'progect_first_app/owner.html', context={'owner': o})