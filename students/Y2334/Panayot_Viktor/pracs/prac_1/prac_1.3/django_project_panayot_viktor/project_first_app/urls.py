from django import VERSION
from django.core.exceptions import ViewDoesNotExist
from django.urls import path
from . import views

urlpatterns = [
    path('owner/<int:id>/', views.detail),
    path('list_view_car_owner/', views.list_view_car_owner),
    path('class_list_view_auto/', views.class_list_view_auto.as_view()),
    path('auto/<int:pk>/', views.auto_view.as_view()),
    path('ownership/', views.CarOwnersListView.as_view()),
    path('car_owner_view/', views.create_view),
    path('auto/<int:pk>/update', views.AutoUpdate.as_view()),
    path('auto/create', views.AutoCreate.as_view(success_url = '/class_list_view_auto/')),
    path('auto/<int:pk>/delete', views.AutoDelete.as_view())
] 