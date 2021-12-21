from django.http import Http404
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

import datetime

from django.shortcuts import render

from project_first_app.models import Owner, ExampleModel, Publisher, Book, Auto


def detail(request):
    context = {}
    try:
        owners = Owner.objects.all()
        context['owners'] = owners
    except Owner.DoesNotExist:
        raise Http404("Poll does not exist")


    return render(request, '../templates/index.html', context)

def list_view(request):
    context ={}
    context["dataset"] = ExampleModel.objects.all()
    return render(request, "../templates/list_view.html", context)

class ExampleList(ListView):
    model = ExampleModel
    template_name = '../templates/cvb_list_view.html'

class PublisherRetrieveView(DetailView):
    model = Publisher

class AllAuto(DetailView):
    model = Auto
    template_name = '../templates/auto.html'

class AllAutos(ListView):
    model = Auto
    template_name = '../templates/autos.html'

class BookListView(ListView):
  model = Book
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

# Create your views here.

def example_view(request):
    # fetch date and time
    now = datetime.datetime.now()
    # convert to string
    html = "Time is {}".format(now)
    # return response
    return HttpResponse(html)
