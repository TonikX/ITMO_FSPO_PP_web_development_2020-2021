from django.urls import path

from . import views
from .views import CarList
from .views import OwnerList
from .views import example_view, CarRetrieveView, addOwner, addCar, CarDelete, CarUpdate, OwnerUpdate

urlpatterns = [
    path('owner/<int:id_owner>/', views.detail),
    path('time/', example_view),
    path('cvb_owner/', OwnerList.as_view()),
    path('cvb_car/', CarList.as_view()),
    path('car/<int:pk>/', CarRetrieveView.as_view()),
    path('add_owner', addOwner),
    path('add_car', addCar),
    path('car/<int:pk>/delete/', CarDelete.as_view()),
    path('car/<int:pk>/update/', CarUpdate.as_view()),
    path('owner/<int:pk>/update/', OwnerUpdate.as_view()),
]


