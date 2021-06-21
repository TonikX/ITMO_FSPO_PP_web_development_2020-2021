"""electricity_metering_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from electricity_accounting_app.views import *

urlpatterns = [
    path("login/", LoginUser.as_view(), name='login'),
    path("register/", RegisterUser.as_view(), name='register'),
    path('logout/', logout_user, name='logout'),
    path('menu/', Menu.as_view(), name='home'),
    path('login/menu/', Menu.as_view()),

    path('renters/', RentersList.as_view()),
    path('renter_detail/<int:pk>/', RentersRetrieveView.as_view()),
    path("renters/create/", RenterCreate.as_view()),
    path('renter_detail/update/<int:pk>/', RenterUpdate.as_view()),
    path('renter_detail/delete/<int:pk>/', RenterDeleteView.as_view()),

    path("adress_list/", AdressList.as_view()),
    path("adress_detail/<int:pk>/", AdressRetrieveView.as_view()),
    path("adress_list/create/", AddressCreate.as_view()),
    path('adress_detail/update/<int:pk>/', AddressUpdate.as_view()),
    path('adress_detail/delete/<int:pk>/', AddressDeleteView.as_view()),

    path("house_list/", HouseList.as_view()),
    path("house_detail/<int:pk>/", HouseRetrieveView.as_view()),
    path("house/create/", HouseCreate.as_view()),
    path('house_detail/update/<int:pk>/', HouseUpdate.as_view()),
    path('house_detail/delete/<int:pk>/', HouseDeleteView.as_view()),

    path("inspector_list/", InspectorList.as_view()),
    path("inspector_detail/<int:pk>/", InspectorRetrieveView.as_view()),
    path("inspector/create/", InspectorCreate.as_view()),
    path('inspector_detail/update/<int:pk>/', InspectorUpdate.as_view()),
    path('inspector_detail/delete/<int:pk>/', InspectorDeleteView.as_view()),

    path("flats/", FlatList.as_view()),
    path("flat_detail/<int:pk>/", FlatRetrieveView.as_view()),
    path("flat/create/", FlatCreate.as_view()),
    path('flat_detail/update/<int:pk>/', FlatUpdate.as_view()),
    path('flat_detail/delete/<int:pk>/', FlatDeleteView.as_view()),

    path("bypass_list/", BypassList.as_view()),
    path("bypass_detail/<int:pk>/", BypassRetrieveView.as_view()),
    path("bypass_list/create/", BypassCreate.as_view()),
    path('bypass_detail/update/<int:pk>/', BypassUpdate.as_view()),
    path('bypass_detail/delete/<int:pk>/', BypassDeleteView.as_view()),
]
