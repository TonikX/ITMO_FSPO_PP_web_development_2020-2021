from django.http import Http404
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from .models import CarOwner, Car
from .forms import CarOwnerForm


class Car_detail(DetailView):
    model = Car

class Car_List(ListView):
    model = Car
    template_name = 'car_list.html'

class CarUpdateView(UpdateView):
    model = Car
    fields = ['number', 'brand', 'model', 'color']
    success_url = '/car/list/'
    template_name = 'car_update.html'

class CarCreate(CreateView):
    model = Car
    template_name = 'create_view.html'
    fields = ['number', 'brand', 'model', 'color']

class CarDelete(DeleteView):
    model = Car
    success_url = '/car/list/'
    template_name = 'car_delete.html'

def owner_list_view(request):
    context = {"dataset": CarOwner.objects.all()}
    return render(request, "owner_list.html", context)


def detail(request, owner_id):
    try:
        p = CarOwner.objects.get(pk=owner_id)
    except CarOwner.DoesNotExist:
        raise Http404("CarOwner does not exist")
    return render(request, 'owner.html', {'owner': p})


def owner_create(request):
    form = CarOwnerForm(request.POST or None)
    if form.is_valid():
        form.save()

    return render(request, 'create_view.html', {'form': form})
