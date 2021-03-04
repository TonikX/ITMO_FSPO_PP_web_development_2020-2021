from django.shortcuts import render
from django.http import Http404
from blog.models import autoOwner
from blog.models import auto
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .forms import ExampleForm # импортируем только-что созданную форму
from django.views.generic.edit import UpdateView
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView


class CarDelete(DeleteView):
    model = auto
    success_url = '/class_cars/'
    template_name = 'car_delete.html'

class CarCreate(CreateView):

   # specify the model for create view
   model = auto
   template_name = 'car_create.html'

   # specify the fields to be displayed

   fields = ['number', 'mark', 'model', 'color']

class CarUpdate(UpdateView):
    model = auto
    fields = ['number', 'mark', 'model', 'color']
    success_url = '/class_cars'
    template_name = 'car_update.html'
    
def create_view(request):
    # dictionary for initial data with 
    # field names as keys
    context ={}
  
    # add the dictionary during initialization
    form = ExampleForm(request.POST or None) # создание экземпляра формы, передача в него данных из формы (из полей в браузере)
    if form.is_valid(): # проверка формы на корректность (валидация)
        form.save()
    context['form'] = form
    return render(request, "create_view.html", context)

class ExampleOwner(DetailView):
    model = autoOwner
    template_name = 'class_owner_detail.html'
  
class ExampleList(ListView):
  
    # specify the model for list view
    model = autoOwner
    template_name = 'cvb_list_view.html'

class CarsList(ListView):
  
    # specify the model for list view
    model = auto
    template_name = 'auto_list.html'

def list_view(request):
    # dictionary for initial data with 
    # field names as keys
    context ={}
  
    # add the dictionary during initialization [en]
    # добавление данных об объектах, полученных в результате выполнения запроса exampleModel.objects.all() в словарь 
    context["dataset"] = autoOwner.objects.all()
          
    return render(request, "list_view.html", context)


# Create your views here.
