from django.http import Http404
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView
from project_first_app.models import CarOwner
from project_first_app.models import Car
from .forms import ExampleForm


# Create your views here.
# def detail(request, owner_id):
#    try:
#        owner = CarOwner.objects.get(pk=owner_id)
#   except CarOwner.DoesNotExist:
#      raise Http404("CarOwner does not exist")
# return render(request, 'owner.html', {'owner': owner})

def list_view(request):
    context = {}
    context["dataset"] = CarOwner.objects.all()

    return render(request, "list_view.html", context)


class ExampleList(ListView):
    # specify the model for list view
    model = Car
    template_name = 'cvb_list_view.html'


class CarRetrieveView(DetailView):
    model = Car


class CarOwnerListView(ListView):
    model = CarOwner
    queryset = model.objects.all()

    def get_queryset(self):
        id = self.request.GET.get('id')

        if id:

            try:
                id = int(id)
                queryset = self.queryset.filter(id=id)

            except ValueError:
                queryset = self.model.objects.none()

            return queryset

        return self.queryset


def create_view(request):
    context = {}

    form = ExampleForm(
        request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "create_view.html", context)


class CarUpdateView(UpdateView):
    model = Car
    fields = ['GovernmentNumber', 'Brand', 'Model', 'Color']
    success_url = '/car/list/'


class CarCreateView(CreateView):
    model = Car
    fields = ['GovernmentNumber', 'Brand', 'Model', 'Color']
    success_url = '/car/list/'


class CarDeleteView(DeleteView):
    model = Car
    success_url = '/car/list/'


