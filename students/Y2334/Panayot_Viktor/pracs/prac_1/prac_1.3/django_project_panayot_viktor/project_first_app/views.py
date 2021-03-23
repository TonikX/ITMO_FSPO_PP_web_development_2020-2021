from django.shortcuts import render
from django.http import Http404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from .models import car_owner, auto, car_ownership
from .forms import CarForm

def detail(request, id):
    try:
        p = car_owner.objects.get(pk=id)
    except car_owner.DoesNotExist:
        raise Http404("car owner does not exist")
    return render(request, 'car_owner.html', {'car_owner': p})

def list_view_car_owner(request):
    text = {}
    text["dataset"] = car_owner.objects.all()
    return render(request, "list_view_car_owner.html", text)

class class_list_view_auto(ListView):
    model = auto
    template_name = 'class_list_view_auto.html'

class auto_view(DetailView):
    model = auto
    template_name = 'auto.html'

class CarOwnersListView(ListView):
    model = car_ownership
    queryset = model.objects.all()
    template_name = 'Ownership.html'

    def get_queryset(self):
        auto = self.request.GET.get('auto')
        
        if auto:
            
            try:
                auto = int('auto')
                queryset = self.queryset.filter(auto = auto)
            except ValueError:
                queryset = self.model.objects.none()
            return queryset
        
        return self.queryset

def create_view(request):
    # dictionary for initial data with 
    # field names as keys
    context ={}
  
    # add the dictionary during initialization
    form = CarForm(request.POST or None) # создание экземпляра формы, передача в него данных из формы (из полей в браузере)
    if form.is_valid(): # проверка формы на корректность (валидация)
        form.save()
    context['form'] = form
    return render(request, "create_view.html", context)

class AutoUpdate(UpdateView):
    model = auto
    fields = ['state_number','mark', 'model', 'color']
    success_url = '/ownership/'
    template_name = 'auto_form.html'

class AutoCreate(CreateView):
    model = auto
    fields = ['state_number','mark', 'model', 'color']
    success_url = '/ownership/'
    template_name = 'auto_create_form.html'

class AutoDelete(DeleteView):
    model = auto
    success_url = '/ownership/'
    template_name = 'auto_delete_form.html'