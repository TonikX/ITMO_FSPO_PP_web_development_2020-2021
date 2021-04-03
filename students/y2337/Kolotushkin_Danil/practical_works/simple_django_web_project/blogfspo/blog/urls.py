from django.urls import path 
from . import views
urlpatterns = [
        path('owner/<int:poll_id>', views.detail),
]
