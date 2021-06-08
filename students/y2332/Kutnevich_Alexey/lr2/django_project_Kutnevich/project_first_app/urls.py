from .views import *
from django.urls import path

urlpatterns = [
    path("owner/<int:owner_id>/", detail1),
    path("owner_list", owner_list_view),
    path("car_list/", CarList.as_view()),
    path('car/<int:pk>/', CarRetrieveView.as_view()),

    path('car/car_list/create', CarListEdit.as_view()),
    path('cars/car_list/update/<int:pk>', CarUpdateView.as_view()),
    path('cars/car_list/delete/<int:pk>', CarDeleteView.as_view()),

    path('owners/owner_list/create/', create_owner),
    path('owners/owner_list/update/<int:pk>', update_owner),
    path('owners/owner_list/delete/<int:pk>', delete_owner)
]