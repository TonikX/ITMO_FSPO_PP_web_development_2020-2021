from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path("Owner/", detail, name='detail'),
    path('Cars/', list_car.as_view()),
    path('Car/<int:pk>/', detail_car.as_view()),
    path('create/', create_view),
    path('Cars/<int:pk>/update/', CarUpdateView.as_view()),
    path('Car/<int:pk>/delete/', CarDeleteView.as_view()),
    path('car/create/', CarCreateView.as_view()),
]
