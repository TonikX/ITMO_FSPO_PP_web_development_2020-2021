from django.shortcuts import render, redirect
from django.http import Http404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView
from blog.models import Owner, Car
from .forms import OwnerCreateForm


def create_owner(request):
    context = {}
    
    form = OwnerCreateForm(
        request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/owner/all/')
        
    context['form'] = form
    return render(request, "owner_form.html", context)


def detail(request, owner_id):
    try:
        owner = Owner.objects.get(pk=owner_id)
    except Owner.DoesNotExist:
        raise Http404("Owner does not exist")
    return render(request, 'detail.html', {"owner": owner})


def owner_list_view(request):
    context = {"dataset": Owner.objects.all()}

    return render(request, "owner_list_view.html", context)


class CarList(ListView):
    model = Car
    template_name = "car_list_view.html"
    

class CarView(DetailView):
    model = Car


class CarUpdateView(UpdateView):
    model = Car
    fields = ['car_number', 'brand', 'model', 'color']
    success_url = '/car/all/'
    

class CarCreateView(CreateView):
    model = Car
    fields = ['car_number', 'brand', 'model', 'color']
    success_url = '/car/all/'


class CarDeleteView(DeleteView):
    model = Car
    success_url = '/car/all/'
