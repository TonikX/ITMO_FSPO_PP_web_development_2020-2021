from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from django import forms
from project_first_app.models import User, Car


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


class UserDetails(DetailView):
    model = User


class UsersList(ListView):
    model = User
    template_name = "users_list.html"


class UserCreateForm(UserCreationForm):
    email = forms.CharField()

    class Meta:
        model = User
        fields = ['PassportNumber',
                  'Name',
                  'Surname',
                  'BirthDate',
                  'Address',
                  'Nationality',
                  'username',
                  'email',
                  'password1',
                  'password2']


class UserCreateView(CreateView):
    model = User
    form_class = UserCreateForm
    success_url = '/users'
