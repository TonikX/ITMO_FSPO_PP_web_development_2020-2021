
from django.shortcuts import render
from django.views.generic import UpdateView, DeleteView, CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .forms import Owner_form

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
def list_view(request):
    context ={}
    context["dataset"]=Car_owner.objects.all()
    return render(request, "progect_first_app/list_view.html", context)
class Car_list(ListView):
    model = Car;
    template_name = "progect_first_app/car_list.html"
class Owner_view(DetailView):
    model = Car_owner
class Car_view(DetailView):
    model = Car
class OwnerCreateView(CreateView):
    model = Car_owner
    fields = [
        "surname",
        "name",
        "date_birth",
    ]
    success_url = 'owner_list'
class CarUpdateView(UpdateView):
    model = Car
    fields = [
        "license_number",
        "brand",
        "car_model",
        "color",
    ]
    success_url = '/car_list/'
class CarDeleteView(DeleteView):
    model = Car
    success_url = "/car_list/"
class CarCreateView(CreateView):
    model = Car
    fields = [
        "license_number",
        "brand",
        "car_model",
        "color",
    ]
    success_url = 'car_list'
class OwnerUpdateView(UpdateView):
    model = Car_owner
    fields = [
        "surname",
        "name",
        "date_birth",
    ]
    success_url = '/owner_list/'
class OwnerDeleteView(DeleteView):
    model = Car_owner
    success_url = "/owner_list/"
