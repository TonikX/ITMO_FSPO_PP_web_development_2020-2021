from django.http import Http404, HttpResponse
from django.shortcuts import render
from datetime import datetime
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView

from .models import AutoOwner
from .models import Auto

from .forms import AddOwnerForm

def owner(request, owner_id):
    try:
        owner = AutoOwner.objects.get(pk=owner_id)
        print('Owner:', owner)
    except AutoOwner.DoesNotExist:
        raise Http404('Poll does not exist')

    return render(request, 'owner.html', {'owner': owner})

class addOwner(CreateView):
    model = AutoOwner
    template_name = 'addOwner.html'

    fields = ['name', 'last_name', 'birthday_date']


class OwnersList(ListView):
    model = AutoOwner
    template_name = 'owners.html'

    def get_queryset(self):
        return self.model.objects.all()

class AutosList(ListView):
    model = Auto
    template_name = 'autos.html'

    def get_queryset(self):
        brand = self.request.GET.get('brand')
        if brand:
            queryset = self.queryset.filter(brand=brand)
            return queryset
        
        return self.model.objects.all()

class AutoRetrieve(DetailView):
    model = Auto
    template_name = 'auto.html'

class AddAuto(CreateView):
    model = Auto
    template_name = 'addAuto.html'

    fields = ['number', 'brand', 'model', 'color']

class RemoveAuto(DeleteView):
    model = Auto
    template_name = 'confirmRemoveAuto.html'
    success_url = '/autos'
