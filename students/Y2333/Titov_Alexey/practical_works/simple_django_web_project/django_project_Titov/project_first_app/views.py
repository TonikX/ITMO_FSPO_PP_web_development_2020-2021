import datetime

from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import OwnerForm
from .models import Owner, Car


# Create your views here.


class CarList(ListView):
    model = Car
    template_name = "car/list.html"


class CarDetail(DetailView):
    model = Car
    template_name = "car/detail.html"


class CarCreate(CreateView):
    model = Car
    fields = ['gos_number', 'mark', 'model', 'color']
    template_name = "car/create.html"
    success_url = '/car/all'


class CarUpdate(UpdateView):
    model = Car
    fields = ['gos_number', 'mark', 'model', 'color']
    template_name = "car/create.html"
    success_url = '/car/all'


class CarDelete(DeleteView):
    model = Car
    template_name = "car/delete.html"
    success_url = '/car/all'



def index(request):
    # fetch date and time
    now = datetime.datetime.now()
    # convert to string
    html = "Time is {}".format(now)
    # return response
    return HttpResponse(html)


def owner(request, owner_id):
    try:
        o = Owner.objects.get(pk=owner_id)

    except Owner.DoesNotExist:
        raise Http404("Owner does not exist")

    return render(request, 'owner/detail.html', {'owner': o})


def owner_create(request):
    form = OwnerForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/owner/all')
    return render(request, 'owner/form.html', {'form': form})


def owner_list(request):
    return render(request, 'owner/list.html', {'owners': Owner.objects.all()})
