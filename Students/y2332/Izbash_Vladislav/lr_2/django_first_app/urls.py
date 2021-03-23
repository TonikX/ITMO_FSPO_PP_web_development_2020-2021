from django.urls import path
from . import views

urlpatterns = [
    path('owner/<int:owner_id>', views.get_owner),
    path('owner/all', views.get_all_owners),
    path('car/all', views.CarList.as_view()),
    path('car/<int:pk>', views.CarInfo.as_view()),
    path('car/all2', views.AltCarList.as_view()),
    path('owner/add', views.add_owner),
    path('car/<int:pk>/update', views.UpdateCar.as_view()),
    path('car/add', views.AddCar.as_view()),
    path('car/<int:pk>/delete', views.DeleteCar.as_view()),
]