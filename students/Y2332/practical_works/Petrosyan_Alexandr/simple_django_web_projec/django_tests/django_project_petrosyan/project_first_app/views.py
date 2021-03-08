from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render

from .models import CarOwner
from .models import Car

from .forms import OwnerForm

#

from .models import ExampleModel
from .models import Publisher
from .models import Book

from .forms import ExampleForm

#

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView

import datetime


# Cars -------------------------------------------------------------------------

def show_home(request):
    return render(request, "home.html")


def show_about(request):
    return render(request, "about.html")


def car_owner_detail(request, owner_id):
    try:
        p = CarOwner.objects.get(pk=owner_id)
    except CarOwner.DoesNotExist:
        raise Http404("Owner does not exist")
    return render(request, 'car_owner_detail.html', {'owner': p})


def owners_list(request):
    context = {"dataset": CarOwner.objects.all()}
    return render(request, "car_owner_list.html", context)


class CarDetailView(DetailView):
    model = Car
    template_name = 'car_detail.html'


class CarsList(ListView):
    model = Car
    template_name = 'car_list.html'


# Cars actions -----------------------------------------------------------------


def create_owner(request):
    context = {}
    form = OwnerForm(request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "car_owner_create.html", context)


class CreateCar(CreateView):
    model = Car
    template_name = 'car_create.html'
    fields = ['number', 'brand', 'model', 'color']
    success_url = '/car/list/'


class UpdateCar(UpdateView):
    model = Car
    template_name = 'car_update.html'
    fields = ['number', 'brand', 'model', 'color']
    success_url = '/car/list/'


class DeleteCar(DeleteView):
    model = Car
    template_name = 'car_delete.html'
    success_url = '/car/list/'


# Examples ---------------------------------------------------------------------


def show_time(request):
    now = datetime.datetime.now().strftime("%H:%M:%S")
    html = "Уже {}, а ты ещё не стал сеньёром".format(now)
    return HttpResponse(html)


def list_view(request):
    context = {"dataset": ExampleModel.objects.all()}
    return render(request, "examples/list_view.html", context)


class ExampleList(ListView):
    model = ExampleModel
    template_name = 'examples/cvb_list_view.html'


class PublisherRetrieveView(DetailView):
    model = Publisher
    template_name = 'examples/publisher_detail.html'


class BookListView(ListView):
    model = Book
    template_name = 'examples/book_list.html'
    queryset = model.objects.all()

    def get_queryset(self):
        publisher = self.request.GET.get('publisher')

        if publisher:
            try:
                publisher = int(publisher)
                queryset = self.queryset.filter(publisher=publisher)
            except ValueError:
                queryset = self.model.objects.none()

            return queryset

        return self.queryset


# Examples actions -------------------------------------------------------------


def create_view(request):
    context = {}
    form = ExampleForm(request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "examples/create_view.html", context)


class PublisherUpdateView(UpdateView):
    model = Publisher
    template_name = 'examples/publisher_update.html'
    fields = ['first_name', 'last_name', 'birthdate']
    success_url = '/publisher/list/'


class ExampleCreate(CreateView):
    model = ExampleModel
    template_name = 'examples/cvb_create_view.html'
    fields = ['title', 'description']


class PublisherCreateView(CreateView):
    model = Publisher
    template_name = 'examples/publisher_create.html'
    fields = ['first_name', 'last_name', 'birthdate']
    success_url = '/publisher/list/'


class PublisherDeleteView(DeleteView):
    model = Publisher
    template_name = 'examples/publisher_delete.html'
    success_url = '/publisher/list/'