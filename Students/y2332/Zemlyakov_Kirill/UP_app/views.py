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

def cov(request, owner_id):
    try: #метод try-except - обработчик исключений
        p = CarOwner.objects.get(pk=owner_id)  #pk - автоматически создается в джанго для любой таблицы в моделе (оно есть у любого объекта из бд), poll_id будет передан функции при её вызове.
#переменной p присваивается объект, полученный в результате выполнения запроса аналогичного "select * from Poll where pk=poll_id"
    except CarOwner.DoesNotExist:
        raise Http404("CarOwner does not exist") #исключение которое будет вызвано, если блок try вернет значение False (не будут найдены записи в таблице Poll)
    return render(request, 'CarOwner.html', {'CarOwner': p}) #данная строка рендерит хтмл страницу detail.html и передает в него объект "p", который в хтмл шаблоне будет называться "poll"


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
    fields=['user','last_name','first_name','birth_date']

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