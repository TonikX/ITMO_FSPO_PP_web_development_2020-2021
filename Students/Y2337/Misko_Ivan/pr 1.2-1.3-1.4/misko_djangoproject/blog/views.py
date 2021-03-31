from django.shortcuts import render
from django.http import Http404
from django.shortcuts import render
from blog.models import Owner
from django.http import HttpResponse
from blog.models import Car
import datetime
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from blog.forms import OwnerForm, CarForm
from django.views.generic.edit import DeleteView
from django.views.generic.edit import UpdateView

def detail(request, id_owner):
    try:
        owner = Owner.objects.get(pk=id_owner)
    except Owner.DoesNotExist:
        raise Http404("Owner does not exist")
    return render(request, 'owner.html', {'owner': owner})

def example_view(request):
    # fetch date and time
    now = datetime.datetime.now()
    # convert to string
    html = "Time is {}".format(now)
    # return response
    return HttpResponse(html)


class OwnerList(ListView):
    # specify the model for list view
    model = Owner
    template_name = 'cvb_owner.html'

class CarList(ListView):
    # specify the model for list view
    model = Car
    template_name = 'cvb_car.html'

class CarRetrieveView(DetailView):
    model = Car
    template_name = 'car_detail.html'


def addOwner(request):
    context = {}
    form = OwnerForm(request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "add_owner.html", context)

def addCar(request):
    context = {}
    form = CarForm(request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "add_car.html", context)

class CarDelete(DeleteView):
    model = Car
    success_url = '/cvb_car/'
    template_name = 'delete_car.html'

class CarUpdate(UpdateView):
    model = Car
    fields = ['state_number', 'brand', 'model', 'color']
    success_url = '/cvb_car'
    template_name = 'update_car.html'

class OwnerUpdate(UpdateView):
    model = Owner
    fields = ['first_name', 'last_name', 'birth_date', 'passport_number', 'home_address', 'nationality']
    success_url = '/cvb_owner'
    template_name = 'update_owner.html'



