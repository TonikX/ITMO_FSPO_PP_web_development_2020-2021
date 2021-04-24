from django.urls import path 
from . import views
from .views import *


urlpatterns = [
        path('owner/<int:poll_id>', views.detail),
        path('owners', views.getOwners),
        path('cars', CarsList.as_view()),
        path('car/<int:pk>', CarView.as_view()),
        path('create_owner', views.createOwnerView),
        path('index', views.index),
        path('<int:pk>/updateCar', updateCarView.as_view()),
        path('create_car', createCarView.as_view(success_url="/cars")),
        path('<int:pk>/delete_car', deleteCarView.as_view()),
]
