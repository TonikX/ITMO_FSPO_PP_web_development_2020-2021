from django.shortcuts import render
from .models import Car_owner, Car
from django.http import  Http404
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .forms import CarOwnerForm
from django.views.generic.edit import UpdateView, CreateView, DeleteView


class CarUpdateView(UpdateView):
  model = Car
  fields = ["license_plate",
            "car_model",
            "car_mark",
            "car_color",]
  success_url = '/car/list/'
  template_name = 'car_update_view.html'

class CarCreateView(CreateView):
  model = Car
  fields = ["license_plate",
            "car_model",
            "car_mark",
            "car_color", ]
  success_url = '/car/list/'
  template_name = 'car_create_view.html'

class CarDeleteView(DeleteView):
  model = Car
  success_url = '/car/list/'
  template_name = 'car_delete_view.html'

def owner_detail(request, car_owner_id):
    try:
        owner = Car_owner.objects.get(pk=car_owner_id)
    except Car_owner.DoesNotExist:
        raise Http404("Owner does not exist")
    return render(request, 'owner.html', {'Owner': owner})

def print_owner_list(request):
    try:
        context={}
        context["owners"] = Car_owner.objects.all()
    except Car_owner.DoesNotExist:
        raise Http404("The ownerlist is empty")
    return render(request, 'ownerlist.html', context)

class CarsDetail(DetailView):
    model = Car
    template_name = 'car_detail.html'

class CarsList(ListView):
    model = Car
    template_name = 'car_list_file.html'


def create_view(request):
    context = {}

    form = CarOwnerForm(request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "create_view.html", context)

