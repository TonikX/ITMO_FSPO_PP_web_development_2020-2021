from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render

from project_first_app.models import CarOwner
from project_first_app.models import Car

from project_first_app.models import ExampleModel
from project_first_app.models import Publisher
from project_first_app.models import Book

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

import datetime

# Cars -------------------------------------------------------------------------

def car_owner_detail(request, owner_id):
    try:
        p = CarOwner.objects.get(pk = owner_id)
    except CarOwner.DoesNotExist:
        raise Http404("Owner does not exist")
    return render(request, 'car_owner_detail.html', {'owner': p})

def owners_list(request):
    context = {}
    context["dataset"] = CarOwner.objects.all()
    return render(request, "car_owners_list.html", context)

class CarDetailView(DetailView):
    model = Car
    template_name = 'car_detail.html'

# TODO: Cars list 

# Examples ---------------------------------------------------------------------

def show_time(request):
    now = datetime.datetime.now().strftime("%H:%M:%S")
    html = "Уже {} а ты ещё не стал сеньёром".format(now)
    return HttpResponse(html)


def list_view(request):
    context = {}
    context["dataset"] = ExampleModel.objects.all()
    return render(request, "list_view.html", context)


class ExampleList(ListView):
    model = ExampleModel
    template_name = 'cvb_list_view.html'

class PublisherRetrieveView(DetailView):
    model = Publisher
    template_name = 'publisher_detail.html'

class BookListView(ListView):
    model = Book
    template_name = 'book_list.html'
    queryset = model.objects.all()

    def get_queryset(self):
        publisher = self.request.GET.get('publisher')

        if publisher:
            try:
                publisher = int(publisher)
                queryset = self.queryset.filter(publisher = publisher)
            except ValueError:
                queryset = self.model.objects.none()

            return queryset

        return self.queryset
