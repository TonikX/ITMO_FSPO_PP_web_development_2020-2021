from django.shortcuts import render
from django.http import Http404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView

from .models import CarOwner, Car, User
from .forms import CarOwnerForm


def get_owner(request, owner_id):
    try:
        owner = CarOwner.objects.get(pk=owner_id)
    except CarOwner.DoesNotExist:
        raise Http404("Car owner does not exist")

    return render(request, 'owner.html', {'owner': owner})


def get_all_owners(request):
    owners = CarOwner.objects.all()

    return render(request, 'owner_list.html', {'owners': owners})


class CarList(ListView):
    model = Car
    template_name = 'car_list.html'


class CarInfo(DetailView):
    model = Car
    template_name = 'car_info.html'


class AltCarList(ListView):
    model = Car,
    template_name = 'car_list.html'
    queryset = Car.objects.all()

    def get_queryset(self):
        brand = self.request.GET.get('brand')

        results = self.queryset.filter(brand=brand)
        return results


def add_owner(request):
    form = CarOwnerForm(request.POST or None)
    if form.is_valid():
        form.save()

    return render(request, 'generic_form.html', {'form': form})


class UpdateCar(UpdateView):
    model = Car
    fields = ['number', 'brand', 'model', 'color']
    success_url = '/car/all'
    template_name = 'update_car.html'


class AddCar(CreateView):
    model = Car
    template_name = 'generic_form.html'
    fields = ['number', 'brand', 'model', 'color']
    success_url = '/car/all'


class DeleteCar(DeleteView):
    model = Car
    template_name = 'generic_delete.html'
    success_url = '/car/all'


class AddUser(CreateView):
    model = User
    template_name = 'generic_form.html'
    fields = ['username', 'password', 'nationality']
    success_url = '/owner/all'
