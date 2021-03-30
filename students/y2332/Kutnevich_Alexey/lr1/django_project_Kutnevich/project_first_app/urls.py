from .views import *
from django.urls import path

urlpatterns = [
    path("owner/<int:owner_id>/", detail1)
]