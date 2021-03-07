from django.views.generic import UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import CreateView
from django.views.generic.edit import DeleteView
from django.http import Http404, HttpResponse
from django.shortcuts import render
from .forms import *


def owner_detail(request, owner_id):
    try:
        owner = Owner.objects.get(id=owner_id)
    except Owner.DoesNotExist:
        raise Http404("Owner does not exist")

    return render(request, 'owner/owner_detail.html', {'owner': owner})


def create_owner(request):
    context = {}
    form = OwnerForm(request.POST or None)

    if form.is_valid():
        form.save()

    context['form'] = form
    return render(request, 'owner/create_owner.html', context)


def list_owners(request):
    context = {}
    context['dataset'] = Owner.objects.all()

    return render(request, 'owner/owner_list_view.html', context)


class CarRetrieveView(DetailView):
    model = Car
    template_name = "car/car_detail.html"


class CarListView(ListView):
    model = Car
    template_name = "car/car_list_view.html"


class CarUpdateView(UpdateView):
    model = Car
    fields = [
        'state_number',
        'brand',
        'model',
        'color'
    ]
    success_url = '/car/list'
    template_name = 'car/car_form.html'


class CarCreateView(CreateView):
    model = Car
    template_name = 'car/car_create_view.html'

    fields = [
        'state_number',
        'brand',
        'model',
        'color'
    ]


class CarDeleteView(DeleteView):
    model = Car
    template_name = 'car/car_confirm_delete.html'
    success_url = '/car/list'
