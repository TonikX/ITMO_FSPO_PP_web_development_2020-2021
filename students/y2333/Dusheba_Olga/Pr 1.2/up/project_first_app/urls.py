from django.urls import path
from . import views

#127.0.0.1:8000/owner/1
urlpatterns = [
    path('owner/<int:owner_id>/', views.detail)
]