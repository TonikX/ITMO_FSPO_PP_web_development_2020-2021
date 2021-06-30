from django.urls import path
from . import views

urlpatterns = [
    path('CarOwner/<int:id>/', views.detail),
]