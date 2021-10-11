from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from .views import *
#from . import views



urlpatterns = [
    path('plane/create', PlanesCreateView.as_view()),
    path('plane/list', Plane_types.as_view()),
    path('plane_type/update/<int:pk>/', PlaneTypesUpdateView.as_view()),
    path('plane_type/delete/<int:pk>/', PlaneTypesDeleteView.as_view()),
    path('clients/list', Clients_list.as_view()),
    path('client/create', ClientsCreateView.as_view()),
    path('client/update/<int:pk>/', ClientsUpdateView.as_view()),
    path('clients/delete/<int:pk>/', ClientsDeleteView.as_view()),
    path('ticket_office/list', Ticket_office_list.as_view()),
    path('ticket_office/create', Ticket_officeCreateView.as_view()),
    path('ticket_office/update/<int:pk>/', Ticket_officeUpdateView.as_view()),
    path('ticket_office/delete/<int:pk>/', Ticket_officeDeleteView.as_view()),
    path('accounts/', include('allauth.urls')),
    path('plane_detail/<int:plane_type_id>/', plane_detail),
    path('client_detail/<int:client_id>/', client_detail),
    path('ticket_office_detail/<int:ticket_office_id>/', ticket_office_detail),
    path('plane/create', plane_view, name='plane'),
    path('client/create', clients_view, name='clients'),
    path('ticket_office/create', ticket_office_view, name='ticket_office'),
    path('plane/list2', ESearchView.as_view(), name='plane_type_list'),
    path('clients/list2', ESearchView_Clients.as_view(), name='clients_list'),
    path('ticket_office/list2', ESearchView_Ticket.as_view(), name='ticket_office_list'),
    #url(r'^search/', include('blog.urls')),
    url(r'^$', ESearchView.as_view(), name='index'),
    url(r'^$', ESearchView_Clients.as_view(), name='index_for_clients'),
    url(r'^$', ESearchView_Ticket.as_view(), name='index_for_ticket'),

]