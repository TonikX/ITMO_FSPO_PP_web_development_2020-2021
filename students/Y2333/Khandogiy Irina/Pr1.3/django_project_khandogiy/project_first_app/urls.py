from django.urls import path
from . import views
from .views import *
from .forms import *

urlpatterns = [
    path('owner/<int:owner_id>/', views.detail),
    path('owner_list/', list_view),
    path('cars_list/', CarsList.as_view()),
    path('cars_list/<int:pk>/', getCar.as_view()),
    #path('owner_list/<int:pk>/', getCarOwner.as_view()),
    path('owner_list/new_owner/', create_owner),
    path('cars_list/<int:pk>/update/', CarUpdateView.as_view()),
    path('cars_list/new_car/', CarCreate.as_view(success_url="cars_list/")),
    path('cars_list/<int:pk>/delete/', CarDeleteView.as_view()),
]


