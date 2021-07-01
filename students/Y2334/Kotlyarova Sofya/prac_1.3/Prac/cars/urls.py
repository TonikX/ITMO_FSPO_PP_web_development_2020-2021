from django.urls import path
from . import views
from .views import CarsView;
from .views import CarView;
from .views import CarUpdateView;
from .views import CarCreateView;
from .views import CarDeleteView;

urlpatterns = [
    path('owners/', views.index),
    path('owners/create', views.create_owner),
    path('cars/', CarsView.as_view()),
    path('cars/create', CarCreateView.as_view()),
    path('cars/<int:pk>', CarView.as_view()),
    path('cars/<int:pk>/update/', CarUpdateView.as_view()),
    path('cars/<int:pk>/delete/', CarDeleteView.as_view()),
]