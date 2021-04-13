from django.urls import path
from . import views

urlpatterns = [
    path('owner/list', views.OwnerListView.as_view()),
    path('owner/create', views.OwnerCreateView.as_view()),
    path('owner/<int:pk>/update', views.OwnerUpdateView.as_view()),
    path('owner/<int:pk>/delete', views.OwnerDeleteView.as_view()),
    path('owner/<int:pk>', views.OwnerDetailView.as_view()),
    path('license/list', views.DriversLicenseListView.as_view()),
    path('license/create', views.DriversLicenseCreateView.as_view()),
    path('license/<int:pk>/update', views.DriversLicenseUpdateView.as_view()),
    path('license/<int:pk>/delete', views.DriversLicenseDeleteView.as_view()),
    path('license/<int:pk>', views.DriversLicenseDetailView.as_view()),
    path('car/list', views.CarListView.as_view()),
    path('car/create', views.CarCreateView.as_view()),
    path('car/<int:pk>/update', views.CarUpdateView.as_view()),
    path('car/<int:pk>/delete', views.CarDeleteView.as_view()),
    path('car/<int:pk>', views.CarDetailView.as_view()),
    path('car_owner/list', views.CarOwnerListView.as_view()),
    path('car_owner/create', views.CarOwnerCreateView.as_view()),
    path('car_owner/<int:pk>/update', views.CarOwnerUpdateView.as_view()),
    path('car_owner/<int:pk>/delete', views.CarOwnerDeleteView.as_view()),
    path('car_owner/<int:pk>', views.CarOwnerDetailView.as_view()),
]
