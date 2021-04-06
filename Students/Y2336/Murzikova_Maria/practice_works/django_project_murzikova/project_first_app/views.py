from django.shortcuts import render
from django.views.generic import ListView
from project_first_app.models import Car
from django.views.generic.detail import DetailView
from .forms import OwnerForm
from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render
from project_first_app.models import Owner
from django.views.generic.edit import UpdateView
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView
def detail(request, owner_id):
    try:
        p = Owner.objects.get(pk=owner_id)
    except Owner.DoesNotExist:
        raise Http404(
            "Owner does not exist")
    return render(request, 'owner.html', {
        'owner': p})

def list_view(request):
    context={}
    context["dataset"]=Owner.objects.all()
    return render(request, "list_view.html", context)


class ExampleList(ListView):
    # specify the model for list view
    model = Car
    template_name = 'cvb_list_view.html'

class CarRetrieveView(DetailView):
    model = Car


class CarListView(ListView):
    model = Car
    queryset = model.objects.all()

    def get_queryset(self):
        owner = self.request.GET.get('owner')

        if owner:

            try:
                owner = int(owner)
                queryset = self.queryset.filter(owner=owner)

            except ValueError:
                queryset = self.model.objects.none()

            return queryset

        return self.queryset


def create_view(request):
    context = {}

    form = OwnerForm(
        request.POST or None)  # создание экземпляра формы, передача в него данных из формы (из полей в браузере)
    if form.is_valid():  # проверка формы на корректность (валидация)
        form.save()
    context['form'] = form
    return render(request, "create_view.html", context)

class CarUpdateView(UpdateView):
  model = Car
  fields = ['id', 'mark', 'model', 'color']
  success_url = '/car/list/'

class CarCreate(CreateView):
   model = Car
   template_name = 'cvb_create_view.html'
   fields = ['id', 'number', 'mark', 'model', 'color']

class CarDeleteView(DeleteView):
  model = Car
  success_url = '/car/list/'