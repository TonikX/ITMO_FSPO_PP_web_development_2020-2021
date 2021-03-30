from django.http import Http404 #импортирует метод обработки ситуации, когда нет    необходимых записей в бд (обработчик ошибок)
from django.shortcuts import render #импортирует метод, который "запускает" созданную хтмл страницу и передает в нее указанные параметры
from UP_app.models import CarOwner,Car,Ownership #импортирует таблицу Poll из модели данных models, где polls - название приложения (и папки)
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import UpdateView
from UP_app.forms import CarOwnerForm

import datetime

class detailCarOwner(DetailView):
    model=CarOwner
    template_name = 'carowner_detail.html'

def carowner_list(request): #CarOwner/view_all
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization [en]
    # добавление данных об объектах, полученных в результате выполнения запроса exampleModel.objects.all() в словарь
    context["dataset"] = CarOwner.objects.all()

    return render(request, "CarOwner.html", context)

def createCarOwner(request):
     context={}
     form=CarOwnerForm(request.POST or None)
     if form.is_valid():
         form.save()
     context['form']=form
     return render(request,"carowner_create.html",context)


class DeleteCarOwner(DeleteView):
    model= CarOwner
    template_name = 'carowner_delete.html'
class UpdateCarOwner(UpdateView):
    model=CarOwner
    template_name = 'carowner_update.html'
    fields=['username','last_name','first_name','birth_date','passport','nationality','address']

#--------------------------------------------------------------------
def eview(request):
    now=datetime.datetime.now()
    html="Time is {}.".format(now)
    return HttpResponse(html)

#--------------------------------------------------------------------
class CarDetail(DetailView):
    model=Car
    template_name = 'car_detail.html'



class CarList(ListView):
    model = Car
    template_name='car_list.html'

class UpdateCar(UpdateView):
    model=Car
    template_name = 'car_update.html'
    fields = ['license_plate_number','car_brand','car_model','car_color']
class CreateCar(CreateView):
    model=Car
    template_name='car_create.html'
    fields = ['license_plate_number','car_brand','car_model','car_color']
class DeleteCar(DeleteView):
    model=Car
    template_name = 'car_delete.html'