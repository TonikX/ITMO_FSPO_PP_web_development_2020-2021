from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from .models import *
from .forms import *
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
import datetime


def detail(request, car_owner_id):
    try:
        owner = CarOwner.objects.get(pk=car_owner_id)
    except:
        raise Http404("Car owner does not exist")

    return render(request, 'owner.html', {'owner': owner})


def all_owners(request):
    context = {}
    try:
        context["owners"] = CarOwner.objects.all()
    except:
        raise Http404("Car owner does not exist")

    return render(request, 'owners.html', context)


def add_owner(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    form = OwnerForm(
        request.POST or None)  # создание экземпляра формы, передача в него данных из формы (из полей в браузере)
    if form.is_valid():  # проверка формы на корректность (валидация)
        form.save()
    context['form'] = form
    return render(request, "add_owner.html", context)


class CarsList(ListView):
    # specify the model for list view
    model = Car
    template_name = 'cars.html'


class CarView(DetailView):
    # specify the model for list view
    model = Car
    template_name = 'car.html'


class CarUpdate(UpdateView):
    model = Car
    template_name = 'car_update.html'
    fields = [
        'number',
        'brand',
        'model',
        'color'
    ]
    success_url = '/cars'


class CarCreate(CreateView):
    model = Car
    template_name = 'car_create.html'
    fields = [
        'number',
        'brand',
        'model',
        'color'
    ]
    success_url = '/cars'


class CarDelete(DeleteView):
    model = Car
    template_name = 'car_delete.html'
    success_url = '/cars'


def time(request):
    now = datetime.datetime.now()

    html = "Time is {}".format(now)

    return HttpResponse(html)


def list_view(request):
    contex = {}

    contex["dataset"] = ExampleModel.objects.all()

    return render(request, "list_view.html", contex)


def create_view(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    form = ExampleForm(
        request.POST or None)  # создание экземпляра формы, передача в него данных из формы (из полей в браузере)
    if form.is_valid():  # проверка формы на корректность (валидация)
        form.save()
    context['form'] = form
    return render(request, "create_view.html", context)


class PublisherUpdateView(UpdateView):
    model = Publisher
    template_name = 'publisher_form.html'
    fields = ['first_name', 'last_name', 'birthdate']
    success_url = '/publisher/list/'


class ExampleList(ListView):
    # specify the model for list view
    model = ExampleModel
    template_name = 'cvb_list_view.html'


class ExampleCreate(CreateView):
    # specify the model for create view
    model = ExampleModel
    template_name = 'cvb_create_view.html'

    # specify the fields to be displayed

    fields = ['title', 'description']


class PublisherCreateView(CreateView):
    model = Publisher
    template_name = 'publisher_form.html'
    fields = ['first_name', 'last_name', 'birthdate']
    success_url = '/publisher/list/'


class PublisherRetrieveView(DetailView):
    model = Publisher
    template_name = 'publisher_detail.html'


class PublisherDeleteView(DeleteView):
    model = Publisher
    template_name = 'publisher_confirm_delete.html'
    success_url = '/publisher/list/'


class BookListView(ListView):
    model = Book
    queryset = model.objects.all()
    template_name = 'book_list.html'

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
