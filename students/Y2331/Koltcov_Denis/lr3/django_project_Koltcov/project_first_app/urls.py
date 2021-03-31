from django.urls import path
from .views import *


urlpatterns = [
    path('CarOwners/', CarOwnersList),
    path('CarOwners/<int:CarOwner_id>/', detail_owner),
    path('CarOwners/create', create_owner),
    path('Car/list', CarListView.as_view()),
    path('Car/create', CarCreateView.as_view()),
    path('Car/<int:pk>/', CarDetail.as_view()),
    path('Car/<int:pk>/update/', CarUpdateView.as_view()),
    path('Car/<int:pk>/delete/', CarDeleteView.as_view()),
]