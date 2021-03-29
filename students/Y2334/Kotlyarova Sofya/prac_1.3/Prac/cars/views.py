from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView

from .models import Owner;
from .models import Car;
from .forms import CreateOwner;

def index(request):
    data = {};
    data["owners"] = Owner.objects.all()
    return render(request, "owners/index.html", data)

class CarsView(ListView):
    model = Car
    template_name = "cars/index.html"

class CarView(DetailView):
    model = Car
    template_name = "cars/show.html"

def create_owner(request):
    context = {}

    form = CreateOwner(
        request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "owners/create.html", context)


class CarUpdateView(UpdateView):
    model = Car
    template_name = "cars/update.html"
    fields = ['number', 'brand', 'model', 'color']
    success_url = '/cars'

class CarCreateView(CreateView):
    model = Car
    template_name = "cars/create.html"
    fields = ['number', 'brand', 'model', 'color']
    success_url = '/cars'

class CarDeleteView(DeleteView):
    model = Car
    template_name = "cars/delete.html"
    success_url = '/cars'