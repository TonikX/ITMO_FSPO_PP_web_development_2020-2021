# # Create your views here.
# from django.http import Http404
# from django.shortcuts import render
#
from django.http import Http404
from django.shortcuts import render

from project_first_app.models import AutoOwner
from project_first_app.models import Auto

from django.http import HttpResponse
import datetime

from django.views.generic.list import ListView
from .models import Auto
from django.views.generic.detail import DetailView

from .forms import AutoOwnerForm
from django.views.generic.edit import UpdateView
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView


def owner(request, owner_id):
    try:
        owner = AutoOwner.objects.get(pk=owner_id)
        print('Owner:', owner)
    except AutoOwner.DoesNotExist:
        raise Http404('Auto owner does not exist')
    return render(request, 'owner.html', {'owner': owner})


def list_view_auto_owner(request):
    text = {"dataset": AutoOwner.objects.all()}
    return render(request, "list_view_auto_owner.html", text)


def auto(request, auto_id):
    try:
        auto = Auto.objects.get(pk=auto_id)
        print('Auto:', auto)
    except Auto.DoesNotExist:
        raise Http404('Auto does not exist')
    return render(request, 'auto.html', {'auto': auto})


def time(request):
    now = datetime.datetime.now()
    html = "Time is: {}".format(now)
    return HttpResponse(html)


class AutoList(ListView):

    model = Auto
    template_name = 'auto_list.html'


class AutoRetrieveView(DetailView):
    model = Auto
    template_name = 'auto_retrieve_view.html'


class AutoListView(ListView):
    model = Auto
    queryset = model.objects.all()
    template_name = 'auto_list_view.html'

    def get_queryset(self):
        Auto = self.request.GET.get('Auto')

        if Auto:

            try:
                Auto = int(Auto)
                queryset = self.queryset.filter(Auto=Auto)

            except ValueError:
                queryset = self.model.objects.none()

            return queryset

        return self.queryset


def create_view(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    form = AutoOwnerForm(
        request.POST or None)  # создание экземпл€ра формы, передача в него данных из формы (из полей в браузере)
    if form.is_valid():  # проверка формы на корректность (валидаци€)
        form.save()
    context['form'] = form
    return render(request, "create_view.html", context)


class AutoUpdateView(UpdateView):
    model = Auto
    fields = ['number', 'brand', 'model', 'color']
    success_url = '../../../auto_list'
    template_name = 'auto_form.html'


class AutoCreate(CreateView):
    model = Auto
    fields = ['number', 'brand', 'model', 'color']
    success_url = '../../../auto_list'
    template_name = 'auto_create.html'


class AutoDeleteView(DeleteView):
    model = Auto
    success_url = '../../../auto_list'
    template_name = 'auto_delete.html'
