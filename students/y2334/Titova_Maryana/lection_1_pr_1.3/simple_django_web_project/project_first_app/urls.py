from django.urls import path
from . import views
from .views import list_view
from .views import ExampleList
from .views import CarRetrieveView
from .views import CarOwnerListView
from .views import CarUpdateView
from .views import CarCreateView
from .views import CarDeleteView
from .views import create_view


urlpatterns = [
    #path('owner/<int:owner_id>/', views.detail),
    path('example_list/', list_view),
    path('car/list/', ExampleList.as_view()),
    path('car/<int:pk>/', CarRetrieveView.as_view()),
    path('owner/list/', CarOwnerListView.as_view()),
    path('example_create', create_view),
    path('car/<int:pk>/update/', CarUpdateView.as_view()),
    path('car/create/', CarCreateView.as_view()),
    path('car/<int:pk>/delete/', CarDeleteView.as_view()),
]