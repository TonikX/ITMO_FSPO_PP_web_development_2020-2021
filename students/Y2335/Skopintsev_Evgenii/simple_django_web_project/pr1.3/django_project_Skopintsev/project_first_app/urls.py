from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('owners/<int:car_owner_id>/', views.detail),
    path('owners/list/', list_owners),
    path('cars/', CarList.as_view()),
    path('cars/<int:pk>/', CarListDetail.as_view()),
    path('owners/create/', create_owner),
    path('cars/<int:pk>/update/', CarUpdate.as_view()),
    path('cars/create/', CarCreate.as_view(success_url="/cars/")),
]
