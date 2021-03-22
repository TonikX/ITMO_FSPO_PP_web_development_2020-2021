
from django.urls import path
from . import views
urlpatterns = [
    path('main/owner_list/owner/<int:owner_id>/', views.owner_detail),
    path('main/owner_list/', views.owner_list),
    path('main/car_list/', views.car_list.as_view()),
    path('main/car_list/car/<int:pk>/', views.car_detail.as_view()),
    path('main/', views.main.as_view()),
    path('main/owner_list/add_owner/', views.add_owner_view),
    path('main/owner_list/update_owner/<int:pk>/', views.update_owner_view.as_view()),
    path('main/car_list/update_car/<int:pk>/', views.update_car_view.as_view()),
    path('main/car_list/add_car/', views.add_car_view.as_view()),
    path('main/owner_list/delete_owner/<int:pk>/', views.delete_owner_view.as_view()),
    path('main/car_list/delete_car/<int:pk>/', views.delete_car_view.as_view()),
]
