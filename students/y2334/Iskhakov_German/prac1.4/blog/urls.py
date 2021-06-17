from django.urls import path
from . import views
from .views import ExampleList
from .views import CarsList
from .views import ExampleOwner
from .views import *

urlpatterns = [
    path('owner/', views.list_view),
    path('class_owner/', ExampleList.as_view()),
    path('class_cars/', CarsList.as_view()),
    path('class_cars/<int:pk>/update/', CarUpdate.as_view()),
    path('class_cars/create', CarCreate.as_view(success_url="/class_cars/")),
    path('class_cars/<int:pk>/delete/', CarDelete.as_view()),
    path('class_owner/<int:pk>/', ExampleOwner.as_view()),
    path('create_owner', views.create_view),
]