from django.urls import path
from . import views
urlpatterns = [
    path('owner/<int:id_owner>/', views.detail),
]

