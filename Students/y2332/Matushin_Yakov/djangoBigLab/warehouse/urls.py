from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import EmployerViewSet, ClientViewSet, ProductionViewSet, SupplierViewSet, BatchViewSet

app_name = "warehouse"
# app_name will help us do a reverse look-up latter.
router = DefaultRouter()
router.register(r'employers', EmployerViewSet)
router.register(r'clients', ClientViewSet)
router.register(r'items', ProductionViewSet)
router.register(r'suppliers', SupplierViewSet)
router.register(r'batches', BatchViewSet)
urlpatterns = [
    path('', include(router.urls)),
]