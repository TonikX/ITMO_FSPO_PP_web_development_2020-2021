from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import *


app_name = "jewelry_fantasy_app"


router = DefaultRouter()
router.register(r'products', ProductionViewSet)
router.register(r'seller', SellerViewSet)
router.register(r'sale', SaleViewSet)
router.register(r'factory', FactoryViewSet)
router.register(r'supply', SupplyViewSet)


urlpatterns = [
   path('', include(router.urls)),
]