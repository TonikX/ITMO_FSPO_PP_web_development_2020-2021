from django.urls import path
from . import views
urlpatterns = [
    path('owners/<int:owner_id>/', views.detail),
]
