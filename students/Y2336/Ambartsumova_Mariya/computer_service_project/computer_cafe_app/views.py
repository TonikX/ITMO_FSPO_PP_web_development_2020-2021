from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from .models import Cafe, Order, Computer
from django.urls import reverse_lazy


class HomeView(ListView):
    model = Cafe
    template_name = 'home.html'


class ComputersListView(ListView):
    model = Computer
    template_name = 'comp.html'
    paginate_by = 3


class AdminOrdersView(ListView):
    model = Order
    template_name = 'admin_view_orders.html'
    paginate_by = 3


class OrdersView(ListView):
    model = Order
    template_name = 'orders.html'
    paginate_by = 3


class MakingOrderView(CreateView):
    model = Order
    template_name = 'makingOrder.html'
    fields = ['user', 'cafe', 'computer', 'online_use', 'game_use', 'time_start', 'time_end', 'comment', 'order_date']
    success_url = reverse_lazy('home')


class OrderDeleteView(DeleteView):
    model = Order
    template_name = 'order_delete.html'
    success_url = reverse_lazy('home')


class OrderUpdateView(UpdateView):
    model = Order
    template_name = 'order_edit.html'
    fields = ['cafe', 'computer', 'online_use', 'game_use', 'time_start', 'time_end', 'comment']
    success_url = reverse_lazy('home')
