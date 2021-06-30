# Create your views here.
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView

from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render

from .models import CarOwner
from .models import Car
from .forms import CarForm

import datetime


def detail(request, owner_id):
    try:
        p = CarOwner.objects.get(pk=owner_id)
    except CarOwner.DoesNotExist:
        raise Http404("Car owner does not exist")
    return render(request, 'detail.html', {'owner': p})


def example_view(request):
    now = datetime.datetime.now()
    html = "Time is {}".format(now)
    return HttpResponse(html)


def list_view(request):
    context = {}

    context["dataset"] = CarOwner.objects.all()

    return render(request, "list_view.html", context)


class ExampleList(ListView):
    model = Car
    template_name = 'cvb_list_view.html'


class CarOwnerList(ListView):
    model = CarOwner
    template_name = 'car_owner_list.html'


class OwnerUpdate(UpdateView):
    model = CarOwner
    fields = ['username', 'first_name', 'last_name', 'bith_date', 'passport_num', 'national', 'address']
    success_url = '/owner/list/'


class OwnerDelete(DeleteView):
    model = CarOwner
    success_url = '/owner/list/'


class OwnerCreate(CreateView):
    model = CarOwner
    fields = ['username', 'first_name', 'last_name', 'bith_date', 'passport_num', 'national', 'address']


class OwnerRetrieveView(DetailView):
    model = CarOwner


class CarRetrieveView(DetailView):
    model = Car


def create_view(request):
    context = {}
    form = CarForm(request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "create_view.html", context)


class CarUpdateView(UpdateView):
    model = Car
    fields = ['gos_number', 'mark', 'model', 'color']
    success_url = '/car/list/'


class CarCreateView(CreateView):
    model = Car
    fields = ['gos_number', 'mark', 'model', 'color']


class CarDeleteView(DeleteView):
    model = Car
    success_url = '/car/list/'
    template_name = 'project_first_app1/car_confirm_delete.html'
