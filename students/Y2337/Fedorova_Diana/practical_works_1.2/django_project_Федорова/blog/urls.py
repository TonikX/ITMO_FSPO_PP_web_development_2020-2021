
from django.urls import path
from . import views

urlpatterns = [
    path('owner/<int:ID_owner>', views.detail),
]
