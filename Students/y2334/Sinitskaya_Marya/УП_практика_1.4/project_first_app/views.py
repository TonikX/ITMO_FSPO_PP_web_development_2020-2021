from django.shortcuts import render
from django.http import Http404, HttpResponse
from project_first_app.models import Owner, User
from project_first_app.models import Car
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView
from .forms import ExampleForm

# Create your views here.
from project_first_app.models import Owner

class CarDelete(DeleteView):
    model = Car
    success_url = '/class_cars/'
    template_name = 'car_delete.html'

class CarCreate(CreateView):
    model = Car
    template_name = 'car_delete.html'
    fields = ['gov_number', 'brand', 'model', 'color']

class CarUpdate(UpdateView):
    model = Car
    fields = ['gov_number', 'brand', 'model', 'color']
    success_url = '/class_cars'
    template_name = 'car_update.html'

def create_view(request):
    context = {}

    form = ExampleForm(request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "create_view.html", context)

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

class ExampleOwner(DeleteView):
    model = Owner
    template_name = 'cvb_list_view.html'

class ExampleList(ListView):

    # specify the model for list view
    model = User
    template_name = 'cvb_list_view.html'

class CarsList(ListView):
    model = Car
    template_name = 'auto_list.html'

def list_view(request):
    context = {}

    context["dataset"] = Owner.objects.all()

    return render(request, "list_view.html", context)

