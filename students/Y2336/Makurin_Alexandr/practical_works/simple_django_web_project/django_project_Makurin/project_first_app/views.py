from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from project_first_app.models import CarOwner, Car


class CarDetails(DetailView):
    model = Car


class CarCreateView(CreateView):
    model = Car
    fields = ['GosNum', 'Brand', 'Model', 'Color']
    success_url = '/cars'


class CarUpdateView(UpdateView):
    model = Car
    fields = ['GosNum', 'Brand', 'Model', 'Color']
    success_url = '/cars'


class CarDeleteView(DeleteView):
    model = Car
    success_url = '/cars'


class CarsList(ListView):
    model = Car
    template_name = "cars_list.html"

    def get_queryset(self):
        Brand = self.request.GET.get("brand")
        queryset = self.model.objects.all()
        if Brand:
            try:
                Brand = str(Brand)
                queryset = queryset.filter(brand=Brand)
            except ValueError:
                queryset = self.model.objects.none()
            return queryset
        return queryset


class OwnerDetails(DetailView):
    model = CarOwner


class OwnersList(ListView):
    model = CarOwner
    template_name = "owners_list.html"


class OwnerCreateView(CreateView):
    model = CarOwner
    fields = ['Name', 'Surname', 'BirthDate']
    success_url = '/owners'
