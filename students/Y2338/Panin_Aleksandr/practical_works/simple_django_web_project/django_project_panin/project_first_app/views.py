from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from .models import Car, CarOwner
from .forms import CarOwnerForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView


def main(request):
    return render(request, 'index.html')


def owner(request, owner_id):
    try:
        p = CarOwner.objects.get(pk=owner_id)
    except CarOwner.DoesNotExist:
        raise Http404("CarOwner does not exist")
    return render(request, 'owner.html', {'owner': p})


def owners(request):
    context = {"dataset": CarOwner.objects.all()}
    return render(request, "owners.html", context)


def create_car_owner(request):
    context = {}
    form = CarOwnerForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/owner")
    context['form'] = form
    return render(request, "create.html", context)


class CarList(ListView):
    model = Car
    template_name = 'cars.html'
    queryset = model.objects.all()

    def get_queryset(self):
        car_id = self.request.GET.get('id')
        if car_id:
            try:
                car_id = int(car_id)
                queryset = self.queryset.filter(id_car=car_id)
            except ValueError:
                queryset = self.model.objects.none()
            return queryset
        return self.queryset


class CarCreateView(CreateView):
    model = Car
    template_name = 'create.html'
    fields = ['state_number', 'brand', 'model', 'color']


class CarView(DetailView):
    model = Car
    template_name = 'car.html'


class CarUpdateView(UpdateView):
    model = Car
    fields = ['state_number', 'brand', 'model', 'color']
    success_url = '/car'


class CarDeleteView(DeleteView):
    model = Car
    success_url = '/car'
