from django.urls import path
from . import views


urlpatterns = [
    path('cars', views.CarsList.as_view()),
    path('cars/create', views.CarCreateView.as_view()),
    path('cars/<int:pk>/', views.CarDetails.as_view()),
    path('cars/<int:pk>/update', views.CarUpdateView.as_view()),
    path('cars/<int:pk>/delete', views.CarDeleteView.as_view()),
    path('owners', views.OwnersList.as_view()),
    path('owners/<int:pk>/', views.OwnerDetails.as_view()),
    path('owners/create', views.OwnerCreateView.as_view()),
]
