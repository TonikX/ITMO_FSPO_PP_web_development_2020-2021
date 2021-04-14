from django.urls import path
from . import views #подключение файла контроллеров,описанного в пункте 3
from .views import *
urlpatterns = [
    path('CarOwner/<int:owner_id>/', views.cov),
    path('current_time/',views.eview),
    path('CarOwner/list/',views.carowner_list),
    path('Car/<int:pk>/',CarDetail.as_view()),
    path('Car/list/',CarList.as_view()),
    path('CarOwner/Create/',views.createCarOwner),
    path('CarOwner/Delete/<int:pk>/',DeleteCarOwner.as_view(success_url="/CarOwner/list")),
    path('CarOwner/Update/<int:pk>/',UpdateCarOwner.as_view(success_url="/CarOwner/list")),
    path('Car/Update/<int:pk>/',UpdateCar.as_view(success_url="/Car/list")),
    path('Car/Create/',CreateCar.as_view(success_url="/Car/list")),
    path('Car/Delete/<int:pk>/',DeleteCar.as_view(success_url='/Car/list'))
    #пример вызова контроллера (функции) с именем "special_case_200" из файда views #пример вызова контроллера (функции) с именем "year_archive" из файда views и передачи в него переменной "year"
]