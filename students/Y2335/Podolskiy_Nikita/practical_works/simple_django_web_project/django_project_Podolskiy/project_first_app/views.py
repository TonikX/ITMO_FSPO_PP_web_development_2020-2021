from django.http import Http404
from project_first_app.models import Owner
from project_first_app.models import Car
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.shortcuts import render
from .forms import add_owner_form
from django.views.generic.edit import UpdateView
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView


def add_owner_view(request):
    context = {}

    form = add_owner_form(
        request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "add_owner.html", context)


class update_owner_view(UpdateView):
  model = Owner
  fields = ['first_name', 'last_name', 'birthdate', 'pass_num', 'address', 'nationality']
  success_url = '/main/owner_list/'
  template_name = 'update_owner.html'


class delete_owner_view(DeleteView):
    model = Owner
    success_url = '/main/owner_list/'
    template_name = 'delete_owner.html'


class add_car_view(CreateView):
    model = Car
    fields = ['state_num', 'brand', 'model', 'color']
    success_url = '/main/car_list/'
    template_name = 'add_car.html'


class update_car_view(UpdateView):
    model = Car
    fields = ['state_num', 'brand', 'model', 'color']
    success_url = '/main/car_list/'
    template_name = 'update_car.html'


class delete_car_view(DeleteView):
    model = Car
    success_url = '/main/car_list/'
    template_name = 'delete_car.html'


def owner_detail(request, owner_id):
    try:
        p = Owner.objects.get(pk=owner_id)
    except Owner.DoesNotExist:
        raise Http404("Owner does not exist")
    return render(request, 'owner_detail.html', {'Owner': p})


def owner_list(request):
    context = {}
    context["dataset"] = Owner.objects.all()
    return render(request, "owner_list.html", context)


class car_list(ListView):
    model = Car
    template_name = 'car_list.html'


class car_detail(DetailView):
    model = Car
    template_name = 'car_detail.html'

class main(ListView):
    model = Car
    template_name = 'main.html'
