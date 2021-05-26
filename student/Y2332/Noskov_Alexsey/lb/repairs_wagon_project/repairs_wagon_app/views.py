from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from .models import Wagon, Worker, Repair
from .forms import WorkerForm, WagonForm, RepairForm

class Menu(ListView):
    model = Worker
    template_name = 'menu.html'

class Menu_reliz(ListView):
    model = Worker
    template_name = 'menu_reliz.html'

class Worker_detail(DetailView):
    model = Worker
    template_name = 'worker_detail.html'

class Worker_List(ListView):
    model = Worker
    template_name = 'worker_list.html'

class WorkerUpdateView(UpdateView):
    model = Worker
    form_class = WorkerForm
    success_url = '/worker/list/'
    template_name = 'worker_update.html'


class WorkerCreate(CreateView):
    model = Worker
    fields = ["username", "password", "tab_number", "fio_worker", "year_worker", "base_worker", "bonus_worker", "number_cart_bank", "brigade"]
    template_name = 'worker_create.html'
    success_url = "/worker/list/"


class WorkerDelete(DeleteView):
    model = Worker
    success_url = '/worker/list/'
    template_name = 'worker_delete.md.html'


class Wagon_detail(DetailView):
    model = Wagon
    template_name = 'wagon_detail.html'


class Wagon_List(ListView):
    model = Wagon
    template_name = 'wagon_list.html'


class WagonUpdateView(UpdateView):
    model = Wagon
    form_class = WagonForm
    success_url = '/wagon/list/'
    template_name = 'wagon_update.html'


class WagonCreate(CreateView):
    model = Wagon
    fields = ["reg_number", "reg_name", "reg_chief", "type", "type_year", "dop_number", "ralway_addressExternal"]
    template_name = 'wagon_create.html'
    success_url = "/wagon/list/"


class WagonDelete(DeleteView):
    model = Wagon
    success_url = '/wagon/list/'
    template_name = 'wagon_delete.html'


class Repair_detail(DetailView):
    model = Repair
    template_name = 'repair_detail.html'


class Repair_List(ListView):
    model = Repair
    template_name = 'repair_list.html'


class RepairUpdateView(UpdateView):
    model = Repair
    form_class = RepairForm
    success_url = '/repair/list/'
    template_name = 'repair_update.html'

class RepairCreate(CreateView):
    model = Repair
    fields = ["resalt", "reason", "cost", "day_start", "day_stop", "type_repair", "schedule", "wagon"]
    template_name = 'repair_create.html'
    success_url = "/repair/list/"


class RepairDelete(DeleteView):
    model = Repair
    success_url = '/repair/list/'
    template_name = 'repair_delete.html'
