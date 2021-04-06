from django.urls import path
from . import views

urlpatterns = [
    path('owner/<int:owner_id>/', views.detail),
    path('owner_list/', views.owner_list_view),
    path('owner/add', views.owner_create),
    path('car/list/', views.Car_List.as_view()),
    path('car/<int:pk>/', views.Car_detail.as_view()),
    path('car/<int:pk>/update/', views.CarUpdateView.as_view()),#http://127.0.0.1:8000/1/update/
    path('car/add/', views.CarCreate.as_view(success_url="/car/list/")), #http://localhost:8000/cvb_example_create
    path('car/<int:pk>/delete/', views.CarDelete.as_view()),
]
