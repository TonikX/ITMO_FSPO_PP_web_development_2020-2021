from django.shortcuts import render
from django.shortcuts import Http404
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.generic.detail import DetailView
from project_first_app.models import Owner, Car
from .forms import OwnerForm


def owner(request, owner_id):
    try:
        selected_owner = Owner.objects.get(pk=owner_id)
    except Owner.DoesNotExist:
        raise Http404("Poll does not exist")
    return render(request, 'project_first_app/owner.html', {'owner': selected_owner})


def owner_list_view(request):
    context = {"owners": Owner.objects.all()}

    return render(request, "project_first_app/owner_list_view.html", context)


def owner_create_view(request):
    context = {}

    form = OwnerForm(request.POST or None)

    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "project_first_app/owner_create.html", context)


class CarView(DetailView):
    model = Car


class CarUpdate(UpdateView):
    model = Car
    fields = ['number_plate', 'brand', 'model', 'color']
    success_url = '/car/list/'


class CarCreate(CreateView):
    model = Car
    fields = ['number_plate', 'brand', 'model', 'color']
    success_url = '/car/list/'


class CarDelete(DeleteView):
    model = Car
    success_url = '/car/list/'


class CarList(ListView):
    model = Car
    template_name = 'project_first_app/car_list_view.html'
