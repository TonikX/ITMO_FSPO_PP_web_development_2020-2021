from django.shortcuts import render
from django.http import Http404
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from project_first_app.forms import Car_ownerForm
from project_first_app.models import Car_owner, Car

def detail(request):
    try:
        p = Car_owner.objects.all()  #вывод всех владельцев в цикле
    except Car_owner.DoesNotExist:
        raise Http404("Car_owner does not exist")# если значение false , то есть значения не найдены в таблице, то будет вызвано исключение
    return render(request, "owner.html", {'owner': p})# создается html страница и передается объект p


class CarView(ListView):
    model = Car
    template_name = 'car.html'


class CarGetID(DetailView):
    model = Car
    template_name = 'car_detail.html'


def car_owner_form(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    form = Car_ownerForm(
        request.POST or None)  # создание экземпляра формы, передача в него данных из формы (из полей в браузере)
    if form.is_valid():  # проверка формы на корректность (валидация)
        form.save()
    context['form'] = form
    return render(request, "owner_form.html", context)


class CarOwnerUpdateView(UpdateView):
    model = Car_owner
    template_name = 'owner_form.html'
    success_url = '../../../owner_form'
    fields = ['surname', 'name', 'date_of_birth']


class CarOwnerDeleteView(DeleteView):
    model = Car_owner
    template_name = 'owner_delete.html'
    success_url = '../../../owner_form'
    fields = ['surname', 'name', 'date_of_birth']

# Create your views here.
