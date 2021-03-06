from django.urls import path

from . import views

urlpatterns = [
    path('home/', views.home),
    path('owner/<int:owner_id>', views.detail),
]
