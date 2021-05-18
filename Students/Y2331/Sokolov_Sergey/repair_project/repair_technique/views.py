from django.contrib.auth.decorators import permission_required, login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views import View
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView

from .forms import *


# Order
class OrderCreate(CreateView):
    model = Order
    form_class = OrderForm
    template_name = 'form.html'


class OrderView(View):
    def get(self, request, *args, **kwargs):
        question = request.GET.get('q')
        if question is not None and question != "":
            search_orders = Order.objects.filter(id=question)
            current_page = Paginator(search_orders, 5)
        else:
            current_page = Paginator(Order.objects.all(), 5)

        page = request.GET.get('page')
        try:
            context = {'orders_set': current_page.page(page)}
        except PageNotAnInteger:
            context = {'orders_set': current_page.page(1)}
        except EmptyPage:
            context = {'orders_set': current_page.page(current_page.num_pages)}

        return render(request, "orders.html", context)


class OrderUpdate(UpdateView):
    model = Order
    form_class = OrderForm
    template_name = 'form.html'


def delete_order(request, id_order):
    order = Order.objects.get(pk=id_order)
    order.delete()
    return redirect('..')


# Customer
class CustomerCreate(CreateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'form.html'


class CustomerView(View):
    def get(self, request):
        question = request.GET.get('q')
        if question is not None and question != "":
            search_customers = Customer.objects.filter(id=question)
            cur_page = Paginator(search_customers, 5)
        else:
            cur_page = Paginator(Customer.objects.all(), 5)

        page = request.GET.get('page')
        try:
            customer = {'customer_set': cur_page.page(page)}
        except PageNotAnInteger:
            customer = {'customer_set': cur_page.page(1)}
        except EmptyPage:
            customer = {'customer_set': cur_page.page(cur_page.num_pages)}

        return render(request, "customers.html", customer)


class CustomerUpdate(UpdateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'form.html'


def delete_customer(request, id_customer):
    customer = Customer.objects.get(pk=id_customer)
    customer.delete()
    return redirect('..')


def customer_orders(request, id_customer):
    context = {}

    technique = Technique.objects.filter(customer=id_customer)
    orders = Order.objects.filter(technique__in=technique)

    context['customer'] = Customer.objects.get(id=id_customer)
    context['order_set'] = orders
    return render(request, 'customer_order.html', context)


# Technique
class TechniqueCreate(CreateView):
    model = Technique
    template_name = 'form.html'
    form_class = TechniqueForm


class TechniqueView(View):
    def get(self, request):
        question = request.GET.get('q')
        if question is not None and question != "":
            search_technique = Technique.objects.filter(id=question)
            cur_page = Paginator(search_technique, 5)
        else:
            cur_page = Paginator(Technique.objects.all(), 5)

        page = request.GET.get('page')
        try:
            technique = {'technique_set': cur_page.page(page)}
        except PageNotAnInteger:
            technique = {'technique_set': cur_page.page(1)}
        except EmptyPage:
            technique = {'technique_set': cur_page.page(cur_page.num_pages)}

        return render(request, "technique.html", technique)


class TechniqueUpdate(UpdateView):
    model = Technique
    form_class = TechniqueForm
    template_name = 'form.html'


def delete_technique(request, id_technique):
    technique = Technique.objects.get(pk=id_technique)
    technique.delete()
    return redirect('..')


# Model
class ModelTechniqueCreate(CreateView):
    model = ModelTechnique
    form_class = ModelForm
    template_name = 'form.html'


class ModelTechniqueView(View):
    def get(self, request):
        question = request.GET.get('q')
        if question is not None and question != "":
            search_models = ModelTechnique.objects.filter(id=question)
            cur_page = Paginator(search_models, 5)
        else:
            cur_page = Paginator(ModelTechnique.objects.all(), 5)

        page = request.GET.get('page')
        try:
            technique_models = {'models_set': cur_page.page(page)}
        except PageNotAnInteger:
            technique_models = {'models_set': cur_page.page(1)}
        except EmptyPage:
            technique_models = {'models_set': cur_page.page(cur_page.num_pages)}

        return render(request, "models.html", technique_models)


class ModelTechniqueUpdate(UpdateView):
    model = ModelTechnique
    form_class = ModelForm
    template_name = 'form.html'


def delete_model(request, id_model):
    technique_model = ModelTechnique.objects.get(pk=id_model)
    technique_model.delete()
    return redirect('..')


# Master
class MasterCreate(CreateView):
    model = Master
    form_class = MasterForm
    template_name = 'form.html'


class MasterView(View):
    def get(self, request, **kwargs):
        question = request.GET.get('q')
        if question is not None and question != "":
            search_masters = Master.objects.filter(id=question)
            cur_page = Paginator(search_masters, 5)
        else:
            cur_page = Paginator(Master.objects.all(), 5)

        page = request.GET.get('page')
        try:
            masters = {'masters_set': cur_page.page(page)}
        except PageNotAnInteger:
            masters = {'masters_set': cur_page.page(1)}
        except EmptyPage:
            masters = {'masters_set': cur_page.page(cur_page.num_pages)}

        return render(request, "masters.html", masters)


class MasterUpdate(UpdateView):
    model = Master
    form_class = MasterForm
    template_name = 'form.html'


def delete_master(request, id_master):
    master = Master.objects.get(pk=id_master)
    master.delete()
    return redirect('..')


# PriceList
class PriceListCreate(CreateView):
    model = PriceList
    form_class = PriceListForm
    template_name = "form.html"


class PriceListView(View):
    def get(self, request):
        question = request.GET.get('q')
        if question is not None and question != "":
            search_service = PriceList.objects.filter(id=question)
            cur_page = Paginator(search_service, 5)
        else:
            cur_page = Paginator(PriceList.objects.all(), 5)

        page = request.GET.get('page')
        try:
            price_list = {'price_list': cur_page.page(page)}
        except PageNotAnInteger:
            price_list = {'price_list': cur_page.page(1)}
        except EmptyPage:
            price_list = {'price_list': cur_page.page(cur_page.num_pages)}

        return render(request, "price_list.html", price_list)


class PriceListUpdate(UpdateView):
    model = PriceList
    form_class = PriceListForm
    template_name = 'form.html'


def delete_price(request, id_price):
    price_list = PriceList.objects.get(pk=id_price)
    price_list.delete()
    return redirect('..')
