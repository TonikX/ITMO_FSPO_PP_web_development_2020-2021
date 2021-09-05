from django.urls import path, include
from . import views
from .views import *


urlpatterns = [
    path('owner/', views.detail, name='detail'),
    path('car/', list_car.as_view()),
    path('Car/<int:pk>/', detail_car.as_view()),
    path('input_owner/', create_view),
    path('create_car/', Car_create.as_view()),
    path('update_car/<int:pk>/update/', Car_update.as_view()),
    path('delete_car/<int:pk>/delete/', Car_delete.as_view()),

]
