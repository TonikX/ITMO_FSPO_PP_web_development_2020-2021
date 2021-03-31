from django.http.response import Http404
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, DeleteView

from .models import CarOwner, CarOwnership, Car, DrivingLicense
from .forms import CarOwnerForm, CarForm
from django.urls import resolve


class CarDeleteView(DeleteView):
  model = Car
  success_url = '/car/'
  template_name = 'delete_view.html'


class CarUpdateView(UpdateView):
    model = Car
    fields = ['gov_number', 'color']
    template_name = 'update_view.html'
    success_url = '/car/'


def create_view(request):
    # dictionary for initial data with 
    # field names as keys
    context = {}

    what = resolve(request.path_info).url_name
    if what == 'create_car':
        form = CarForm(request.POST or None)
    elif what == 'create_owner':
        form = CarOwnerForm(request.POST or None)
    else:
        raise Http404('Type in parameters')

    if form.is_valid(): # проверка формы на корректность (валидация)
        form.save()
    context['form'] = form
    
    return render(request, "create_view.html", context)


def owners_info(request, gov_number):
    try:
        carOwnership = CarOwnership.objects.get(id_car=Car.objects.get(gov_number=gov_number))
    except CarOwnership.DoesNotExist:
        raise Http404('Car Ownership is not found')
    return render(request, 'owner.html', {'owner': carOwnership.id_owner})


class CarListView(ListView):
    model = Car
    queryset = model.objects.all()

    def get_queryset(self):
        license = self.request.GET.get('license')
        car_id = self.request.GET.get('id')

        if car_id:
            try:
                queryset = self.queryset.filter(id=car_id)
            except ValueError:
                queryset = self.model.objects.none()
            return queryset

        if license:
            try:
                owner = DrivingLicense.objects.get(license_number=license).id_owner
                queryset = self.queryset.filter(carowner=owner)
            except ValueError:
                queryset = self.model.objects.none()
                
            return queryset

        return self.queryset
