"""autobase_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter

from autobase_app.views import DriverViewSet, MotorDepotViewSet, GarageViewSet, CarViewSet, \
    FuelViewSet, WaybillAPIView, WaybillDetailAPIView, RefuelAPIView, RefuelDetailAPIView

router = SimpleRouter()

router.register(r'drivers', DriverViewSet)
router.register(r'motor-depots', MotorDepotViewSet)
router.register(r'garages', GarageViewSet)
router.register(r'cars', CarViewSet)
router.register(r'fuels', FuelViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^auth/', include('djoser.urls')),
    url(r'^auth/', include('djoser.urls.authtoken')),
    path('waybills/', WaybillAPIView.as_view()),
    path('waybills/<int:pk>/', WaybillDetailAPIView.as_view()),
    path('refuels/', RefuelAPIView.as_view()),
    path('refuels/<int:pk>/', RefuelDetailAPIView.as_view()),
] + router.urls
