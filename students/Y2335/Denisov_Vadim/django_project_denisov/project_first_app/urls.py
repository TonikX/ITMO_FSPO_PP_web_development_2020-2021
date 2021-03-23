from django.urls import path
from . import views
from .views import *


urlpatterns = [
    path('owner/<int:owner_id>/', views.detail),
    path('owners/', owners),
    path('cars/', car_list.as_view()),
    path('car/<int:pk>/', car.as_view()),
    path('car_view/', cars.as_view()),
    path('create_owner/', create_view),
    path('car/<int:pk>/update/', Car_update.as_view()),
    path('create_car/', Car_create.as_view(success_url="/cars/")),
    path('car/<int:pk>/delete/', Car_delete.as_view()),
]