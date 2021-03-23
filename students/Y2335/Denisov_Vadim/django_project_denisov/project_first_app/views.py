from django.http import Http404
from project_first_app.models import Owner, Car
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .forms import Owner_form
from django.views.generic.edit import UpdateView
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView


# Create your views here.
def detail(request, owner_id):
    try:
        p = Owner.objects.get(pk=owner_id)
    except Owner.DoesNotExist:
        raise Http404("Owner does not exist")
    return render(request, 'Owner.html', {'Owner': p})


def owners(request):
    context = {"owner_list": Owner.objects.all()}
    return render(request, "owners.html", context)


class car_list(ListView):
    model = Car
    template_name = 'car_list.html'


class car(DetailView):
    model = Car
    template_name = 'car_view.html'


class cars(ListView):
    model = Car
    queryset = model.objects.all()

    def get_queryset(self):
        car_id = self.request.GET.get('car_id')

        if car_id:

            try:
                car_id = int(car_id)
                queryset = self.queryset.filter(car_id=car_id)

            except ValueError:
                queryset = self.model.objects.none()

            return queryset

        return self.queryset

    template_name = 'cars.html'


def create_view(request):
    # dictionary for initial data with
    # field names as keys
    context = {}
    # add the dictionary during initialization
    form = Owner_form(request.POST or None)
    # создание экземпляра формы, передача в него данных из формы (из полей в браузере)
    if form.is_valid():  # проверка формы на корректность (валидация)
        form.save()
    context['form'] = form
    return render(request, "create_owner.html", context)


class Car_update(UpdateView):
    model = Car
    fields = ["State_number", "Brand", "Model", "Color"]
    success_url = '/cars/'
    template_name = 'update_car.html'


class Car_create(CreateView):
    model = Car
    template_name = 'create_car.html'
    fields = ['id', 'State_number', 'Brand', 'Model', 'Color']


class Car_delete(DeleteView):
    model = Car
    success_url = '/cars/'
    template_name = 'delete_car.html'