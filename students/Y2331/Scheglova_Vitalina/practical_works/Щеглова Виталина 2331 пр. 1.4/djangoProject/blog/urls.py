from django.urls import path
from .views import list_view
from .views import example_view
from .views import ExampleList
from .views import *
from .views import Owner
from .views import create_view

#Практика 5

urlpatterns = [
    path('car/<int:pk>/update/', CarUpdateView.as_view()), #'car/<int:pk>/update/' - отображение urlа в поисковой строке браузера,
    path('car/<int:pk>/delete/', CarDeleteView.as_view()),
    path('example_car', create_view),
    path('example_create', create_view),
    path('7/cars/list/', CarListView.as_view()),
    path('owner_example/', Owner.as_view()),
    path('publisher/<int:pk>/', PublisherRetrieveView.as_view()),
    path('сvb_example/', ExampleList.as_view()),
    path('example_list/', list_view),
    path('time/', example_view),
    path('owner_list', Owner.as_view()),

]
