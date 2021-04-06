from django.urls import path
from . import views
urlpatterns = [
    path('carowner/<int:owner_id>/', views.detail),
]