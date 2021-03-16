from django.urls import path
from . import views #подключение файла контроллеров,описанного в пункте 3
urlpatterns = [
    path('', views.startPage),
    path('carOwner/<int:carOwner_id>', views.detail), #пример вызова контроллера (функции) с именем "special_case_200" из файда views
     #пример вызова контроллера (функции) с именем "year_archive" из файда views и передачи в него переменной "year"
]