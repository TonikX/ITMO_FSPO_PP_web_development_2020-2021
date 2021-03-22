from django.urls import path
from . import views


urlpatterns = [
    path('ownerlist/', views.print_owner_list),
    path('owner/<int:car_owner_id>/', views.owner_detail),
    path('car/<int:pk>/', views.CarsDetail.as_view()),
    path('car/list/', views.CarsList.as_view()),
    path('carowner/add/', views.create_view),
    path('car/add/', views.CarCreateView.as_view()),
    path('car/<int:pk>/remove/', views.CarDeleteView.as_view()),
    path('car/<int:pk>/update/', views.CarUpdateView.as_view()),
]