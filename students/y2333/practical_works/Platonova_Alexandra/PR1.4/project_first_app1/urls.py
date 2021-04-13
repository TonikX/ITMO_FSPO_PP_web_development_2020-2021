from django.urls import path
from project_first_app1 import views
from .views import example_view
from .views import list_view
from .views import ExampleList
from .views import CarRetrieveView
from .views import create_view
from .views import CarUpdateView
from .views import CarCreateView
from .views import CarDeleteView
from .views import CarOwnerList
from .views import OwnerCreate
from .views import OwnerDelete
from .views import OwnerUpdate
from .views import OwnerRetrieveView

urlpatterns = [
    path('owner/<int:owner_id>/', views.detail),
    path('time/', example_view),
    path('example_list/', list_view),
    path('car/<int:pk>/', CarRetrieveView.as_view()),
    path('owner/<int:pk>/', OwnerRetrieveView.as_view()),
    path('car/list/', ExampleList.as_view()),
    path('car/create', create_view),
    path('car/<int:pk>/update/', CarUpdateView.as_view()),
    path('create_car/', CarCreateView.as_view(success_url='/car/list/')),
    path('car/<int:pk>/delete/', CarDeleteView.as_view()),
    path('owner/list/', CarOwnerList.as_view()),
    path('owner/<int:pk>/update/', OwnerUpdate.as_view()),
    path('create_owner/', OwnerCreate.as_view(success_url='/owner/list/')),
    path('owner/<int:pk>/delete/', OwnerDelete.as_view()),

]


