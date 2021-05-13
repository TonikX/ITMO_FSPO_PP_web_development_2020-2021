from django.urls import path
from . import views
from .views import * #CarView, CarGetID, CarOwnerUpdateView, CarOwnerDeleteView, car_owner_form

urlpatterns = [
    # path('owner/<int:id_owner>/', views.detail), #вызывается функция контроллер с названием detail и передает переменную id_owner
    path('owner/', views.detail), 
    path('car/', CarView.as_view()), 
    path('car/<int:pk>/', CarGetID.as_view()), 
    path('owner_form/', car_owner_form),
    path('owner_form/<int:pk>/update/', CarOwnerUpdateView.as_view()),
    path('owner_form/<int:pk>/delete/', CarOwnerDeleteView.as_view()),
]

