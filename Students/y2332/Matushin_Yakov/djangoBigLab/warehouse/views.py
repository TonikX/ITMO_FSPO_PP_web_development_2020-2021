from rest_framework import viewsets, permissions
from .models import Employer, Client, Supplier, Production, Batch
from .serializers import EmployerSerializer, ClientSerializer, SupplierSerializer, ProductionSerializer, BatchSerializer


class EmployerViewSet(viewsets.ModelViewSet):
    serializer_class = EmployerSerializer
    queryset = Employer.objects.all()
    permission_classes = permissions.IsAuthenticatedOrReadOnly,


class ClientViewSet(viewsets.ModelViewSet):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()
    permission_classes = permissions.IsAuthenticatedOrReadOnly,


class SupplierViewSet(viewsets.ModelViewSet):
    serializer_class = SupplierSerializer
    queryset = Supplier.objects.all()
    permission_classes = permissions.IsAuthenticatedOrReadOnly,


class ProductionViewSet(viewsets.ModelViewSet):
    serializer_class = ProductionSerializer
    queryset = Production.objects.all()
    permission_classes = permissions.IsAuthenticatedOrReadOnly,


class BatchViewSet(viewsets.ModelViewSet):
    serializer_class = BatchSerializer
    queryset = Batch.objects.all()
