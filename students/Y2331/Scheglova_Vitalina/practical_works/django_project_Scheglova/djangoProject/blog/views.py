from django.shortcuts import render
from django.views.generic import CreateView
from django.views.generic.list import ListView
from .forms import PlaneForm, ClientsForm, Ticket_officeForm
from django.views.generic import UpdateView, DeleteView
from .models import Plane_type, Client, Ticket_office
from django.http import Http404
from django.views import View
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage



class Plane_types(ListView):
    model = Plane_type
    template_name = 'plane_type_list.html'

class PlanesCreateView(CreateView):
    model = Plane_type
    form_class = PlaneForm
    template_name = 'plane.html'
    success_url = '/plane/list2'

class PlaneTypesUpdateView(UpdateView):
    model = Plane_type
    form_class = PlaneForm
    template_name = 'plane_update.html'
    success_url = '/plane/list'

class PlaneTypesDeleteView(DeleteView):
    model = Plane_type
    form_class = PlaneForm
    template_name = 'plane_delete.html'
    success_url = '/plane/list'

class Clients_list(ListView):
    model = Client
    template_name = 'clients_list.html'

class ClientsCreateView(CreateView):
    model = Client
    form_class = ClientsForm
    template_name = 'clients.html'
    success_url = '/clients/list2'

class ClientsUpdateView(UpdateView):
    model = Client
    form_class = ClientsForm
    template_name = 'clients_update.html'
    success_url = '/clients/list'

class ClientsDeleteView(DeleteView):
    model = Client
    form_class = ClientsForm
    template_name = 'clients_delete.html'
    success_url = '/plane/list'

class Ticket_office_list(ListView):
    model = Ticket_office
    template_name = 'ticket_office_list.html'

class Ticket_officeCreateView(CreateView):
    model = Ticket_office
    form_class = Ticket_officeForm
    template_name = 'ticket_office.html'
    success_url = 'list2'

class Ticket_officeUpdateView(UpdateView):
    model = Ticket_office
    form_class = Ticket_officeForm
    template_name = 'ticket_office_update.html'
    success_url = 'ticket_office/list'

class Ticket_officeDeleteView(DeleteView):
    model = Ticket_office
    form_class = Ticket_officeForm
    template_name = 'ticket_office_delete.html'
    success_url = 'ticket_office/list'

def plane_detail(request, plane_type_id):
    try:
        p = Plane_type.objects.get(pk=plane_type_id)
    except Plane_type.DoesNotExist:
        raise Http404("Plane_type does not exist")
    return render(request, 'plane_detail.html', {'plane_type': p})

def client_detail(request, client_id):
    try:
        p = Client.objects.get(pk=client_id)
    except Client.DoesNotExist:
        raise Http404("Client does not exist")
    return render(request, 'client_detail.html', {'client': p})

def ticket_office_detail(request, ticket_office_id):
    try:
        p = Ticket_office.objects.get(pk=ticket_office_id)
    except Ticket_office.DoesNotExist:
        raise Http404("Ticket office does not exist")
    return render(request, 'ticket_office_detail.html', {'ticket_office': p})

def plane_view(request):
    return render(request, 'plane.html')

def clients_view(request):
    return render(request, 'clients.html')

def ticket_office_view(request):
    return render(request, 'ticket_office.html')


# Представление сделано на основе класса View

class Plane_pagination(View):

    def get(self, request):
        context = {}
        # Забираем все опубликованные статье отсортировав их по дате публикации
        all_plane_types = Plane_type.objects.order_by('id')
        # Создаём Paginator, в который передаём статьи и указываем,
        # что их будет 10 штук на одну страницу
        current_page = Paginator(all_plane_types, 3)

        # Pagination в django_bootstrap3 посылает запрос вот в таком виде:
        # "GET /?page=2 HTTP/1.0" 200,
        # Поэтому нужно забрать page и попытаться передать его в Paginator,
        # для нахождения страницы
        page = request.GET.get('page')
        try:
            # Если существует, то выбираем эту страницу
            context['plane_type_list'] = current_page.page(page)
        except PageNotAnInteger:
            # Если None, то выбираем первую страницу
            context['plane_type_list'] = current_page.page(1)
        except EmptyPage:
            # Если вышли за последнюю страницу, то возвращаем последнюю
            context['plane_type_list'] = current_page.page(current_page.num_pages)

        print('context[plane_type_list] ', context)

        return render(request, 'plane_type_list.html', context)

class Clients_pagination(View):

    def get(self, request):
        context = {}
        # Забираем все опубликованные статье отсортировав их по дате публикации
        all_clients = Client.objects.order_by('id')
        # Создаём Paginator, в который передаём статьи и указываем,
        # что их будет 10 штук на одну страницу
        current_page = Paginator(all_clients, 3)

        # Pagination в django_bootstrap3 посылает запрос вот в таком виде:
        # "GET /?page=2 HTTP/1.0" 200,
        # Поэтому нужно забрать page и попытаться передать его в Paginator,
        # для нахождения страницы
        page = request.GET.get('page')
        try:
            # Если существует, то выбираем эту страницу
            context['clients_list'] = current_page.page(page)
        except PageNotAnInteger:
            # Если None, то выбираем первую страницу
            context['clients_list'] = current_page.page(1)
        except EmptyPage:
            # Если вышли за последнюю страницу, то возвращаем последнюю
            context['clients_list'] = current_page.page(current_page.num_pages)

        print('context[clients_list] ', context)

        return render(request, 'clients_list.html', context)

class Ticket_office_pagination(View):

    def get(self, request):
        context = {}
        # Забираем все опубликованные статье отсортировав их по дате публикации
        all_offices = Ticket_office.objects.order_by('id')
        # Создаём Paginator, в который передаём статьи и указываем,
        # что их будет 10 штук на одну страницу
        current_page = Paginator(all_offices, 3)

        # Pagination в django_bootstrap3 посылает запрос вот в таком виде:
        # "GET /?page=2 HTTP/1.0" 200,
        # Поэтому нужно забрать page и попытаться передать его в Paginator,
        # для нахождения страницы
        page = request.GET.get('page')
        try:
            # Если существует, то выбираем эту страницу
            context['ticket_office_list'] = current_page.page(page)
        except PageNotAnInteger:
            # Если None, то выбираем первую страницу
            context['ticket_office_list'] = current_page.page(1)
        except EmptyPage:
            # Если вышли за последнюю страницу, то возвращаем последнюю
            context['ticket_office_list'] = current_page.page(current_page.num_pages)

        print('context[ticket_office_list] ', context)

        return render(request, 'ticket_office_list.html', context)

class ESearchView(View):
    template_name = 'index.html' #что это

    def get(self, request, *args, **kwargs):
        context = {}

        question = request.GET.get('q')
        if question is not None:
            plane_type_list = Plane_type.objects.filter(model_name__search=question)
            print('blog_plane_type', plane_type_list)

            # формируем строку URL, которая будет содержать последний запрос
            # Это важно для корректной работы пагинации
            #context['last_question'] = '?q=%s' % question
        else:
            plane_type_list = Plane_type.objects.order_by('id')

        current_page = Paginator(plane_type_list, 10)

        page = request.GET.get('page')
        try:
            context['plane_type_list'] = current_page.page(page)
        except PageNotAnInteger:
            context['plane_type_list'] = current_page.page(1)
        except EmptyPage:
            context['plane_type_list'] = current_page.page(current_page.num_pages)
        print('ddd', context['plane_type_list'])

        return render(request, 'plane_type_list.html', context)


class ESearchView_Clients(View):
    template_name = 'index_for_clients.html' #что это

    def get(self, request, *args, **kwargs):
        context = {}

        question = request.GET.get('q')
        if question is not None:
            clients_list = Client.objects.filter(FIO_client__search=question)#возможно это
            print('blog_client', clients_list)

            # формируем строку URL, которая будет содержать последний запрос
            # Это важно для корректной работы пагинации
            #context['last_question'] = '?q=%s' % question
        else:
            clients_list = Client.objects.order_by('id')

        current_page = Paginator(clients_list, 10)

        page = request.GET.get('page')
        try:
            context['clients_list'] = current_page.page(page)
        except PageNotAnInteger:
            context['clients_list'] = current_page.page(1)
        except EmptyPage:
            context['clients_list'] = current_page.page(current_page.num_pages)
        print('ddd', context['clients_list'])

        return render(request, 'clients_list.html', context)


class ESearchView_Ticket(View):
    template_name = 'index_for_ticket.html' #что это

    def get(self, request, *args, **kwargs):
        context = {}

        question = request.GET.get('q')
        if question is not None:
            ticket_office_list = Ticket_office.objects.filter(ticket_office_adress__search=question)#возможно это
            print('blog_ticket_office', ticket_office_list)

            # формируем строку URL, которая будет содержать последний запрос
            # Это важно для корректной работы пагинации
            #context['last_question'] = '?q=%s' % question
        else:
            ticket_office_list = Ticket_office.objects.order_by('id')

        current_page = Paginator(ticket_office_list, 10)

        page = request.GET.get('page')
        try:
            context['ticket_office_list'] = current_page.page(page)
        except PageNotAnInteger:
            context['ticket_office_list'] = current_page.page(1)
        except EmptyPage:
            context['ticket_office_list'] = current_page.page(current_page.num_pages)
        print('ddd', context['ticket_office_list'])

        return render(request, 'ticket_office_list.html', context)
