from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('owners/<int:car_owner_id>/', views.detail),
    path('owners/list/', list_owners),
    path('cars/list/', CarList.as_view()),
    path('cars/<int:pk>/', CarListDetail.as_view()),
]
