from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from electricity_accounting_app.forms import *
from django.shortcuts import render
from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views import View


class Menu(ListView):
    model = Inspector
    template_name = 'home.html'


class RentersList(ListView):
    paginate_by = 3
    model = Renter
    template_name = 'renter_list.html'


class RentersRetrieveView(DetailView):
    model = Renter
    template_name = 'renter_detail.html'


class RenterCreate(CreateView):
    model = Renter
    fields = '__all__'
    template_name = 'renter_create.html'
    success_url = '/renters/'


class RenterUpdate(UpdateView):
    model = Renter
    form_class = RenterForm
    template_name = "renter_update.html"
    success_url = '/renters/'


class RenterDeleteView(DeleteView):
    model = Renter
    template_name = "renter_delete.html"
    success_url = '/renters/'


class AdressList(ListView):
    paginate_by = 3
    model = Adress
    template_name = 'adress_list.html'


class AdressRetrieveView(DetailView):
    model = Adress
    template_name = 'adress_detail.html'


class AddressCreate(CreateView):
    model = Adress
    fields = '__all__'
    template_name = 'address_create.html'
    success_url = '/adress_list/'


class AddressUpdate(UpdateView):
    model = Adress
    form_class = AdressForm
    template_name = "adress_update.html"
    success_url = '/adress_list/'


class AddressDeleteView(DeleteView):
    model = Adress
    template_name = "address_delete.html"
    success_url = '/adress_list/'


class HouseList(ListView):
    paginate_by = 3
    model = House
    template_name = 'house_list.html'


class HouseRetrieveView(DetailView):
    model = House
    template_name = 'house_detail.html'


class HouseCreate(CreateView):
    model = House
    fields = '__all__'
    template_name = 'house_create.html'
    success_url = '/house_list/'


class HouseUpdate(UpdateView):
    model = House
    form_class = HouseForm
    template_name = "house_update.html"
    success_url = '/house_list/'


class HouseDeleteView(DeleteView):
    model = House
    template_name = "house_delete.html"
    success_url = '/house_list/'


class InspectorList(ListView):
    paginate_by = 3
    model = Inspector
    template_name = 'inspector_list.html'


class InspectorRetrieveView(DetailView):
    model = Inspector
    template_name = 'inspector_detail.html'


class InspectorCreate(CreateView):
    form_class = CreateInspectorForm
    template_name = 'inspector_create.html'
    success_url = '/inspector_list/'


class InspectorUpdate(UpdateView):
    model = Inspector
    form_class = InspectorFormUpdate
    template_name = "inspector_update.html"
    success_url = '/inspector_list/'


class InspectorDeleteView(DeleteView):
    model = Inspector
    template_name = "inspector_delete.html"
    success_url = '/inspector_list/'


class FlatList(ListView):
    paginate_by = 3
    model = Flat
    template_name = 'flat_list.html'


class FlatRetrieveView(DetailView):
    model = Flat
    template_name = 'flat_detail.html'


class FlatCreate(CreateView):
    model = Flat
    fields = '__all__'
    template_name = 'flat_create.html'
    success_url = '/flats/'


class FlatUpdate(UpdateView):
    model = Flat
    form_class = FlatForm
    template_name = "flat_update.html"
    success_url = '/flats/'


class FlatDeleteView(DeleteView):
    model = Flat
    template_name = "flat_delete.html"
    success_url = '/flats/'


class BypassList(ListView):
    paginate_by = 3
    model = Bypass
    template_name = 'bypass_list.html'


class BypassRetrieveView(DetailView):
    model = Bypass
    template_name = 'bypass_detail.html'


class BypassCreate(CreateView):
    model = Bypass
    fields = '__all__'
    template_name = 'bypass_create.html'
    success_url = '/bypass_list/'


class BypassUpdate(UpdateView):
    model = Bypass
    form_class = BypassForm
    template_name = "bypass_update.html"
    success_url = '/bypass_list/'


class BypassDeleteView(DeleteView):
    model = Bypass
    template_name = "bypass_delete.html"
    success_url = '/bypass_list/'


class RegisterUser(CreateView):
    form_class = RegisterInspectorForm
    template_name = 'register.html'
    success_url = 'http://127.0.0.1:8000/menu/'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('http://127.0.0.1:8000/menu/')


class LoginUser(LoginView):
    form_class = LoginInspectorForm
    template_name = "login.html"

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('http://127.0.0.1:8000/menu/')