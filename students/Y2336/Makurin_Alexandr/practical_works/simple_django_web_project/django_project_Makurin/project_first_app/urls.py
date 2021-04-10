from django.urls import path
from . import views


urlpatterns = [
    path('cars', views.CarsList.as_view()),
    path('cars/create', views.CarCreateView.as_view()),
    path('cars/<int:pk>/', views.CarDetails.as_view()),
    path('cars/<int:pk>/update', views.CarUpdateView.as_view()),
    path('cars/<int:pk>/delete', views.CarDeleteView.as_view()),
    path('users', views.UsersList.as_view()),
    path('users/<int:pk>/', views.UserDetails.as_view()),
    path('users/create', views.UserCreateView.as_view()),
]
