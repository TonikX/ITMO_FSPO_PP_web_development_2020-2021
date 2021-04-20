from django.db.models import fields
from django.shortcuts import render
from django.http import Http404, HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from .models import AutoOwner, Auto, DriversLicense, Owner

# Create your views here.


def index(request):
    return render(request, 'project_first_app/index.html')


class AutoDetailView(DetailView):
    model = Auto
    template_name = "project_first_app/auto_detail.html"


class AutoListView(ListView):
    model = Auto
    template_name = "project_first_app/auto_list.html"


class AutoUpdateView(UpdateView):
    model = Auto
    fields = [
        'license_plate',
        'brand',
        'model',
        'color',
    ]
    template_name = 'project_first_app/auto_form.html'
    success_url = '/auto/list'


class AutoCreateView(CreateView):
    model = Auto
    fields = [
        'license_plate',
        'brand',
        'model',
        'color',
    ]
    success_url = '/auto/list'


class AutoDeleteView(DeleteView):
    model = Auto
    template_name = 'project_first_app/auto_confirm_delete.html'
    success_url = '/auto/list'


class OwnerListView(ListView):
    model = Owner
    template_name = "project_first_app/owner_list.html"


class OwnerCreateView(CreateView):
    model = Owner
    fields = [
        'last_name',
        'first_name',
        'birth_date',
    ]
    success_url = '/owner/list'


class OwnerUpdateView(UpdateView):
    model = Owner
    fields = [
        'last_name',
        'first_name',
        'birth_date',
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


class AutoOwnerListView(ListView):
    model = AutoOwner
    template_name = "project_first_app/auto_owner_list.html"


class AutoOwnerCreateView(CreateView):
    model = AutoOwner
    fields = [
        'owner_id',
        'auto_id',
        'start_date',
        'end_date',
    ]
    success_url = '/auto_owner/list'


class AutoOwnerUpdateView(UpdateView):
    model = AutoOwner
    fields = [
        'owner_id',
        'auto_id',
        'start_date',
        'end_date',
    ]
    template_name = 'project_first_app/autoowner_form.html'
    success_url = '/auto_owner/list'


class AutoOwnerDeleteView(DeleteView):
    model = AutoOwner
    template_name = 'project_first_app/auto_owner_confirm_delete.html'
    success_url = '/auto_owner/list'


class AutoOwnerDetailView(DetailView):
    model = AutoOwner
    template_name = "project_first_app/auto_owner_detail.html"


