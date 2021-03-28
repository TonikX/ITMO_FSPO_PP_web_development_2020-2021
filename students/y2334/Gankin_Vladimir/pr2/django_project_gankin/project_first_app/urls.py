from django.urls import path
from . import views

urlpatterns = [
    path('owner/<int:owner_id>', views.owner),
    path('auto/<int:auto_id>', views.auto)
]
