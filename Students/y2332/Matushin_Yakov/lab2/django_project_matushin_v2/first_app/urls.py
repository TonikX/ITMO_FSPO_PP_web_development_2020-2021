from django.urls import path
from . import views

# подключение файла контроллеров,описанного в пункте 3
from .views import list_view, create_view, AutoList, AutoRetrieveView, AutoUpdateView, AutoCreateView, AutoDeleteView

urlpatterns = [
    path('owner/<int:owner_id>/', views.detail), #пример вызова контроллера (функции) с именем "year_archive" из файда views и передачи в него переменной "year"
    path('owner/', list_view),
    path('auto/list/', AutoList.as_view()),
    path('auto/<int:pk>/', AutoRetrieveView.as_view()),
    path('owner/create/', create_view),
    path('auto/<int:pk>/update/', AutoUpdateView.as_view()),
    path('auto/create/', AutoCreateView.as_view(success_url="/auto/list/")),  # success_url
    path('auto/<int:pk>/delete/', AutoDeleteView.as_view()),
]


