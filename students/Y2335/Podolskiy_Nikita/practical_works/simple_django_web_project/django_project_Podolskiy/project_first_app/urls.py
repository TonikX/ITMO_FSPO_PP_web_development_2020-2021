
from django.urls import path
from . import views
urlpatterns = [
    path('Owner/<int:owner_id>/', views.detail),
]
