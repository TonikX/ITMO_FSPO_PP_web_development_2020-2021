from django.http import Http404
from django.shortcuts import render
from .models import CarOwner, Car
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from .forms import OwnerForm


def detail(request, owner_id):
    try:
        owner = CarOwner.objects.get(pk=owner_id)
    except CarOwner.DoesNotExist:
        raise Http404("Poll does not exist")
    return render(request, 'owner.html', {'owner': owner})


def owners_list(request):
    context = {"dataset": CarOwner.objects.all()}
    return render(request, "owners_list.html", context)


class CarsList(ListView):
    model = Car
    template_name = 'cars_list.html'


class CarDetail(DetailView):
    model = Car
    template_name = 'car_detail.html'


class UpdateCar(UpdateView):
    model = Car
    template_name = 'car_update.html'
    fields = ['number', 'brand', 'model', 'color']
    success_url = '/cars/list'


def create_owner(request):
    context = {}
    form = OwnerForm(request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "create_owner.html", context)


class CreateCar(CreateView):
    model = Car
    template_name = 'car_create.html'
    fields = ['number', 'brand', 'model', 'color']
    success_url = '/cars/list'


class DeleteCar(DeleteView):
    model = Car
    template_name = 'car_delete.html'
    success_url = '/cars/list'
