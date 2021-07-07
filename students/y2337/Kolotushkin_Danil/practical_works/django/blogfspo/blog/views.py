from django.shortcuts import render
from django.http import Http404 
from django.shortcuts import render
from blog.models import owner
from blog.models import car
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView

from .forms import OwnerForm

def detail(request, poll_id):
    try: 
        p = owner.objects.get(pk=poll_id)
    except owner.DoesNotExist:
        raise Http404("owner does not exist")
    return render(request, 'owner.html', {'owner': p}) 

def index(request):
    return render(request, 'index.html')

def getOwners(request):
    objects = {}
    objects["dataset"] = owner.objects.all()
    return render(request, "owners_list.html", objects)

class CarsList(ListView):
    model = car
    template_name = "cars_list.html"

class CarView(DetailView):
    model = car
    template_name = "car.html"

def createOwnerView(request):
    context = {}

    form = OwnerForm(request.POST or None)

    if form.is_valid():
        form.save()
    context["form"] = form;
    return render(request, "createView.html", context)

class updateCarView(UpdateView):
    model = car
    fields = ["gov_number", "brand", "model", "color"]
    success_url = "/cars"

class createCarView(CreateView):
    model = car
    template_name = "create_car.html"
    fields = ["gov_number", "brand", "model", "color"]

class deleteCarView(DeleteView):
    model = car
    success_url = "/cars"
