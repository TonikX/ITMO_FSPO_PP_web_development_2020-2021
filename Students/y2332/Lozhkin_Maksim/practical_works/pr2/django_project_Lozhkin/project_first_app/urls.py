from django.urls import path
from .views import *
urlpatterns = [
    path('owner/<int:owner_id>/', detail),
    path('owner/list', owners_list),
    path('cars/list', CarsList.as_view()),
    path('car/<int:pk>', CarDetail.as_view()),
    path('car/<int:pk>/update', UpdateCar.as_view()),
    path('owner/create', create_owner),
    path('car/create', CreateCar.as_view()),
    path('car/<int:pk>/delete', DeleteCar.as_view())
]