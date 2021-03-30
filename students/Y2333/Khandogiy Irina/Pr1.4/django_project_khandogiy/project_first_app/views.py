from msilib.schema import ListView

from django.http import Http404

from django.shortcuts import render
from django.views.generic.list import ListView
from project_first_app.models import *
from django.shortcuts import render
from django.views.generic.detail import DetailView
from .forms import *
from django.views.generic.edit import UpdateView, CreateView, DeleteView



# функция для получения информации о владельце по id
def detail(request, owner_id):
    try:
        c = CarOwner.objects.get(pk=owner_id)
    except CarOwner.DoesNotExist:
        raise Http404("CarOwner does not exist")
    return render(request, "first_app/owner.html", {'owner': c})


# представление на основе функции
def list_view(request):
    context = {}
    context["dataset"] = CarOwner.objects.all()

    return render(request, "first_app/carowner_view.html", context)


# представление на основе класса
class CarsList(ListView):
    model = Car
    template_name = 'first_app/car_list.html'


# экземпляр машины
class getCar(DetailView):
    model = Car
    template_name = 'first_app/getCar.html'


# экземпляр владельца
class getCarOwner(DetailView):
    model = CarOwner
    template_name = 'first_app/getOwner.html'


# какая-то фигня пока что
class OwnerListView(ListView):
    model = CarOwner
    queryset = model.objects.all()

    def get_queryset(self):
        lic = DriverLicense.request.GET.get(id=id)

        if lic:

            try:
                lic = int(lic)
                queryset = self.queryset.filter(lic=lic)

            except ValueError:
                queryset = self.model.objects.none()

            return queryset

        return self.queryset


# форма на основе функции
def create_owner(request):
    context = {}
    form = OwnerForm(
        request.POST or None)  # создание экземпляра формы, передача в него данных из формы (из полей в браузере)
    if form.is_valid():  # проверка формы на корректность (валидация)
        form.save()
    context['form'] = form
    return render(request, "first_app/ownerForm.html", context)
    success_url = '/owner_list/'


# форма на основе класса
# обновление
class CarUpdateView(UpdateView):
    model = Car
    fields = ['gov_number', 'brand', 'model', 'color']
    template_name = 'first_app/carForm.html'
    success_url = '/cars_list/'


# создание объекта
class CarCreate(CreateView):

    model = Car
    template_name = 'first_app/carCreate.html'

    fields = ['gov_number', 'brand', 'model', 'color']


# удаление объекта
class CarDeleteView(DeleteView):
    model = Car
    template_name = 'first_app/carDelete.html'
    success_url = '/cars_list/'
