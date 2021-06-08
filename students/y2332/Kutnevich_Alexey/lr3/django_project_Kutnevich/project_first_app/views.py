from django.http import Http404
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from .forms import *
from project_first_app.models import CarOwner
from project_first_app.models import Car
from django.views.generic.edit import UpdateView
from project_first_app.models import DriveCard
from project_first_app.models import Own


def detail1(request, owner_id):
    try:
        owner = CarOwner.objects.get(pk=owner_id)
    except CarOwner.DoesNotExist:
        raise Http404("Poll does not exist")
    return render(request, 'owner.html', {'owner': owner})


def owner_list_view(request):
    context = {"dataset": CarOwner.objects.all()}
    return render(request, "owner_list.html", context)


class CarList(ListView):
    model = Car
    template_name = 'car_list.html'


class CarRetrieveView(DetailView):
    model = Car
    template_name = 'car_detail.html'


class CarListEdit(CreateView):
    model = Car
    fields = '__all__'
    template_name = 'car_edit.html'
    success_url = '/car_list/'


class CarUpdateView(UpdateView):
    template_name = "car_update.html"
    model = Car
    fields = '__all__'
    success_url = '/car_list/'


class CarDeleteView(DeleteView):
    template_name = "car_delete.html"
    model = Car
    success_url = '/car_list/'


def create_owner(request):
    context = {}
    form = CreateOwnerForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("/owner_list/")

    context['form'] = form
    return render(request, "owner_create.html", context)


def update_owner(request, pk):
    context = {}
    owner = CarOwner.objects.get(pk=pk)
    form = UpdateOwnerForm(request.POST or None, instance=owner)
    if form.is_valid():
        form.save()
        return redirect("/owner_list/")

    context['form'] = form
    return render(request, "owner_update.html", context)


def delete_owner(request, pk):
    context = {}
    owner = CarOwner.objects.get(pk=pk)
    form = OwnerDelete(request.POST or None)
    if form.is_valid():
        owner.delete()
        return redirect("/owner_list/")

    context['form'] = form
    return render(request, "owner_delete.html", context)