from django.urls import path
from . import views
from .views import example_view
from .views import list_view
from .views import ExampleList
from .views import *

urlpatterns = [
    path('owners/', views.detail), #пример вызова контроллера (функции) с именем "special_case_200" из файда views
    path('autos/', AllAutos.as_view()), #пример вызова контроллера (функции) с именем "special_case_200" из файда views
    path('auto/<int:pk>/', AllAuto.as_view()), #пример вызова контроллера (функции) с именем "year_archive" из файда views и передачи в него переменной "year"
    path('time/', example_view),
    path('example_list/', list_view),
    path('сvb_example/', ExampleList.as_view()),
    path('publisher/<int:pk>/', PublisherRetrieveView.as_view()),
    path('book/list/', BookListView.as_view()),
]
