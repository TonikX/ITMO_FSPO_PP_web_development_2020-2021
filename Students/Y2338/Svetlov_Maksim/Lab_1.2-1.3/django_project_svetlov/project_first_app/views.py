from django.db.models import fields
from django.shortcuts import render
from django.http import Http404, HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from .models import CarOwner, Car, DriversLicense, Owner


class CarDetailView(DetailView):
    model = Car
    template_name = "project_first_app/car_detail.html"


class CarListView(ListView):
    model = Car
    template_name = "project_first_app/car_list.html"


class CarUpdateView(UpdateView):
    model = Car
    fields = [
        'license_plate',
        'brand',
        'model',
        'color',
    ]
    template_name = 'project_first_app/car_form.html'
    success_url = '/car/list'


class CarCreateView(CreateView):
    model = Car
    fields = [
        'license_plate',
        'brand',
        'model',
        'color',
    ]
    success_url = '/car/list'


class CarDeleteView(DeleteView):
    model = Car
    template_name = 'project_first_app/car_confirm_delete.html'
    success_url = '/car/list'


class OwnerListView(ListView):
    model = Owner
    template_name = "project_first_app/owner_list.html"


class OwnerCreateView(CreateView):
    model = Owner
    fields = [
        'username',
        'password',
        'last_name',
        'first_name',
        'birth_date',
        'nationality',
        'passport_number',
        'address',

    ]
    success_url = '/owner/list'


class OwnerUpdateView(UpdateView):
    model = Owner
    fields = [
        'username',
        'password',
        'last_name',
        'first_name',
        'birth_date',
        'nationality',
        'passport_number',
        'address',
    ]
    template_name = 'project_first_app/owner_form.html'
    success_url = '/owner/list'


class OwnerDeleteView(DeleteView):
    model = Owner
    template_name = 'project_first_app/owner_confirm_delete.html'
    success_url = '/owner/list'


class OwnerDetailView(DetailView):
    model = Owner
    template_name = "project_first_app/owner_detail.html"


class DriversLicenseListView(ListView):
    model = DriversLicense
    template_name = "project_first_app/drivers_license_list.html"


class DriversLicenseCreateView(CreateView):
    model = DriversLicense
    fields = [
        'owner_id',
        'license_number',
        'type',
        'date_issue',
    ]
    success_url = '/license/list'


class DriversLicenseUpdateView(UpdateView):
    model = DriversLicense
    fields = [
        'owner_id',
        'license_number',
        'type',
        'date_issue',
    ]
    template_name = 'project_first_app/driverslicense_form.html'
    success_url = '/license/list'


class DriversLicenseDeleteView(DeleteView):
    model = DriversLicense
    template_name = 'project_first_app/drivers_license_confirm_delete.html'
    success_url = '/license/list'


class DriversLicenseDetailView(DetailView):
    model = DriversLicense
    template_name = "project_first_app/drivers_license_detail.html"


class CarOwnerListView(ListView):
    model = CarOwner
    template_name = "project_first_app/car_owner_list.html"


class CarOwnerCreateView(CreateView):
    model = CarOwner
    fields = [
        'owner_id',
        'car_id',
        'start_date',
        'end_date',
    ]
    success_url = '/car_owner/list'


class CarOwnerUpdateView(UpdateView):
    model = CarOwner
    fields = [
        'owner_id',
        'car_id',
        'start_date',
        'end_date',
    ]
    template_name = 'project_first_app/carowner_form.html'
    success_url = '/car_owner/list'


class CarOwnerDeleteView(DeleteView):
    model = CarOwner
    template_name = 'project_first_app/car_owner_confirm_delete.html'
    success_url = '/car_owner/list'


class CarOwnerDetailView(DetailView):
    model = CarOwner
    template_name = "project_first_app/car_owner_detail.html"
