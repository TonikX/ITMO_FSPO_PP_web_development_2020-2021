from django.urls import path
from . import views

urlpatterns = [
    path('owner/<int:carowner_id>', views.carowner),
    path('owners/', views.all_owners),
    path('cars/', views.CarListView.as_view()),
    path('cars/<int:pk>', views.CarDetailView.as_view()),

    path('owners/create/', views.create_owner),

    path('cars/create', views.CarCreateView.as_view()),
    path('cars/update/<int:pk>', views.CarUpdateView.as_view()),
    path('cars/delete/<int:pk>', views.CarDeleteView.as_view()),
]
