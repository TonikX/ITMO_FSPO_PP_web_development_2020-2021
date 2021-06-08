from rest_framework import routers
from django.urls import path, include
from check_in_app import views
from .views import *


app_name = "check_in_app"


urlpatterns = [
    path('hostels/all', views.HostelListView.as_view()),
    path('hostels/all/<int:pk>/', views.HostelRetrieveAPIView.as_view()),
    path('payments/all', PaymentListView.as_view()),
    path('payments/all/<int:pk>/', PaymentsRetrieveView.as_view()),
    path('payments/create/', PaymentCreateAPIView.as_view()),
    path('payments/update/<int:pk>/', PaymentUpdate.as_view()),
    path('residents/all', ResidentList.as_view()),
    path('residents/create', ResidentCreateView.as_view()),
    path('residents/update/<int:pk>/', ResidentUpdate.as_view()),
    path('residents/all/<int:pk>/', ResidentRetrive.as_view()),
    path('checkin/all', CheckInListView.as_view()),
    path('checkin/create', CheckInCreate.as_view()),
    path('checkin/delete/<int:pk>/', CheckinDelete.as_view()),
    path('checkin/update/<int:pk>/', CheckinUpdate.as_view()),
    path('rooms/all', RoomListView.as_view()),
    path('rooms/update/<int:pk>/', RoomUpdate.as_view()),
    ]
