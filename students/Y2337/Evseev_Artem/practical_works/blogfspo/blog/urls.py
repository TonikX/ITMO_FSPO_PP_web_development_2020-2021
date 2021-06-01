from django.urls import path
from . import views
from .views import CarList
from .views import CarView
from .views import CarCreateView
from .views import CarUpdateView
from .views import CarDeleteView

urlpatterns = [
    path('owner/<int:owner_id>/', views.detail),
    path('owner/all/', views.owner_list_view),
    path('car/<int:pk>/', CarView.as_view()),
    path('car/all/', CarList.as_view()),
    path('car/<int:pk>/edit/', CarUpdateView.as_view()),
    path('car/<int:pk>/delete/', CarDeleteView.as_view()),
    path('car/create/', CarCreateView.as_view()),
    path('create_car/', CarCreateView.as_view()),
    path('owner/create/', views.create_owner),
    path('create_owner/', views.create_owner),
]