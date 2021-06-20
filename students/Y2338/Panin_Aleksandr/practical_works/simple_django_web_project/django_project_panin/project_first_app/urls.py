from django.urls import path
from . import views
urlpatterns = [
    path('', views.main),
    path('owner', views.owners),
    path('owner/create/', views.create_car_owner),
    path('owner/<int:owner_id>/', views.owner),
    path('car', views.CarList.as_view()),
    path('car/create/', views.CarCreateView.as_view(success_url="/car")),
    path('car/<int:pk>/', views.CarView.as_view()),
    path('car/<int:pk>/update/', views.CarUpdateView.as_view()),
    path('car/<int:pk>/delete/', views.CarDeleteView.as_view()),
]
