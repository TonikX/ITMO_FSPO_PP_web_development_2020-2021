from django.http import Http404
from django.shortcuts import render
from .models import CarOwner
from .models import Car
from .forms import OwnerForm

from django.views.generic.list import ListView

from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView


def detail_owner(request, CarOwner_id):
    try:
        p = CarOwner.objects.get(pk=CarOwner_id)
    except CarOwner.DoesNotExist:
        raise Http404("Owner does not exist")
    return render(request, 'project_first_app/CarOwner_detail.html', {'CarOwner': p})


class CarDetail(DetailView):
    model = Car


def CarOwnersList(request):
    context = {"CarOwners": CarOwner.objects.all()}

    return render(request, "project_first_app/CarOwner_list.html", context)


class CarListView(ListView):
    model = Car
    queryset = model.objects.all()

    def get_queryset(self):
        owner = self.request.GET.get('owner')

        if owner:

            try:
                owner = int(owner)
                queryset = self.queryset.filter(owner=owner)

            except ValueError:
                queryset = self.model.objects.none()

            return queryset

        return self.queryset


def create_owner(request):

    context = {}

    form = OwnerForm(
        request.POST or None)
    if form.is_valid():  # проверка формы на корректность (валидация)
        form.save()
    context['form'] = form
    return render(request, "project_first_app/CreateOwner.html", context)


class CarDeleteView(DeleteView):
    model = Car
    success_url = '/Car/list'


class CarUpdateView(UpdateView):
    model = Car
    fields = ['number', 'brand', 'model', 'color']
    success_url = '/Car/list'

class CarCreateView(CreateView):
    model = Car
    template_name = 'project_first_app/CreateCar.html'
    fields = ['number', 'brand', 'model', 'color']
    success_url = '/Car/list'