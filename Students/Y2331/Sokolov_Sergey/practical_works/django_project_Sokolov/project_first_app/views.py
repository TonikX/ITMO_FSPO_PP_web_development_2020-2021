from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .forms import OwnerForm
from .models import CarOwner, Car
from django.conf import settings

import datetime


def cur_time(request):
    now = datetime.datetime.now()
    html = "Time is {}".format(now)
    return HttpResponse(html)


# Methods for owners
def create_owner(request):
    context = {}
    form = OwnerForm(request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "owner_create.html", context)


def detail(request, owner_id):
    try:
        owner = CarOwner.objects.get(pk=owner_id)
    except CarOwner.DoesNotExist:
        raise Http404("Нет такого владельца")
    return render(request, 'owner.html', {"owner": owner})


def owners(request):
    context = {"dataset": CarOwner.objects.all()}
    return render(request, "owners.html", context)


# Class forms for Car
class CarCreate(CreateView):
    model = Car
    fields = ['brand', 'model', 'colour', 'state_number']
    success_url = '.'


class CarView(DetailView):
    model = Car


class CarList(ListView):
    model = Car
    queryset = model.objects.all()

    def get_queryset(self):
        car = self.request.GET.get('car')

        if car:
            try:
                car = int(car)
                queryset = self.queryset.filter(car=car)

            except ValueError:
                queryset = self.model.objects.none()

            return queryset

        return self.queryset


class CarUpdate(UpdateView):
    model = Car
    fields = ['brand', 'model', 'colour', 'state_number']
    success_url = '..'


class CarDelete(DeleteView):
    model = Car
    success_url = '../..'
