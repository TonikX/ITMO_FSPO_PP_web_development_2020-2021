from django.urls import path
from . import views

urlpatterns = [
    path('car/get/<int:pk>/', views.CarView.as_view()),
    path('car/create/', views.CarCreate.as_view()),
    path('car/update/<int:pk>/', views.CarUpdate.as_view()),
    path('car/delete/<int:pk>/', views.CarDelete.as_view()),
    path('car/list/', views.CarList.as_view()),
    path('owner/list/', views.owner_list_view),
    path('owner/create/', views.owner_create_view),
    path('owner/get/<int:owner_id>/', views.owner),
]
