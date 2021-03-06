from django.urls import path
from . import views
urlpatterns = [
    path('owner/<int:carowner_id>/', views.owner, name = "owner"),
    path('owner_list/', views.list_view, name="owner_list"),
    path('car_list/', views.Car_list.as_view(), name="car_list"),
    path('car_owner/<int:pk>/', views.Owner_view.as_view()),
    path('car/<int:pk>/', views.Car_view.as_view(), name = "details"),
    path('create_owner', views.OwnerCreateView.as_view(), name ="create_ow"),
    path('car_owner/<int:pk>/update', views.OwnerUpdateView.as_view(), name = "up_owner"),
    path('car_owner/<int:pk>/delete', views.OwnerDeleteView.as_view(), name = "del_owner"),
    path('create_car', views.CarCreateView.as_view(), name ="create_car"),
    path('car/<int:pk>/update', views.CarUpdateView.as_view(), name = "up_car"),
    path('car/<int:pk>/delete', views.CarDeleteView.as_view(), name = "del_car"),
]