from django.urls import path
from . import views
from .views import list_view, CarList, CarView, OwnerView, OwnerList

#127.0.0.1:8000/owner/1
urlpatterns = [
    # path('owner/<int:owner_id>/', views.detail),
    path('list/', list_view),
    path('car_list_view/', CarList.as_view()),
    path('owner_list_view/', OwnerList.as_view()),
    path('car/<int:pk>/', CarView.as_view()),
    path('owner/<int:pk>/', OwnerView.as_view()),
    path('car/<int:pk>/update', views.CarUpdateView.as_view(), name="update_car"),
    path('car/<int:pk>/delete', views.CarDeleteView.as_view(), name="delete_car"),
    path('create_car/', views.CarCreateView.as_view(), name="create_car"),
    path('owner/<int:pk>/update', views.OwnerUpdateView.as_view(), name="update_owner"),
    path('owner/<int:pk>/delete', views.OwnerDeleteView.as_view(), name="delete_owner"),
    path('create_owner/', views.OwnerCreateView.as_view(), name="create_owner"),
]
