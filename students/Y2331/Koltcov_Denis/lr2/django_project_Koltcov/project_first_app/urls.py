from django.urls import path
from . import views
urlpatterns = [
    path('CarOwner/<int:CarOwner_id>', views.detail_owner),
    path('Car/<int:Car_id>', views.detail_car),
]