from django.shortcuts import render
from django.http import Http404
from project_first_app.models import  Car_owner

def detail(request, id_owner):
    try:
        c = Car_owner.objects.get(pk = id_owner)
    except Car_owner.DoesNotExist:
        raise Http404("Car_owner does not exist")
    return render(request, "owner.html", {'owner': c})
# Create your views here.
