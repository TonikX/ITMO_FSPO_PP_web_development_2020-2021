from django.urls import path
from . import views
from .views import CarUpdateView, CarOwnerUpdateView, CarDeleteView, CarOwnerDeleteView

urlpatterns = [
    path('listOwners/', views.listOwners),
    path('listOwners/<int:id>/', views.owner),
    path('listCars/', views.listCars),
    path('listCars/<int:id>/', views.car),
    path('listOwners/createOwner/', views.create_owner),
    path('listCars/createCar/', views.create_car),
    path('listCars/<int:pk>/update/', CarUpdateView.as_view()),
    path('listOwners/<int:pk>/update/', CarOwnerUpdateView.as_view()),
    path('listCars/<int:pk>/delete/', CarDeleteView.as_view()),
    path('listOwners/<int:pk>/delete/', CarOwnerDeleteView.as_view()),

]
