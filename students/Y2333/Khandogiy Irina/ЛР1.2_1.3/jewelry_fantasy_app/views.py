from rest_framework import generics
from rest_framework import viewsets, permissions
from django.shortcuts import render
from .models import *
from .serializers import *

# Create your views here.


class ProductionViewSet(viewsets.ModelViewSet):
    serializer_class = ProductionSerializer
    queryset = Production.objects.all()
    permission_classes = permissions.IsAuthenticatedOrReadOnly


class SellerViewSet(viewsets.ModelViewSet):
    serializer_class = SellerSerializer
    queryset = Seller.objects.all()
    permission_classes = permissions.IsAuthenticatedOrReadOnly


class SaleViewSet(viewsets.ModelViewSet):
    serializer_class = SaleSerializer
    queryset = Sale.objects.all()
    permission_classes = permissions.IsAuthenticatedOrReadOnly


class FactoryViewSet(viewsets.ModelViewSet):
    serializer_class = FactorySerializer
    queryset = Factory.objects.all()
    permission_classes = permissions.IsAuthenticatedOrReadOnly


class SupplyViewSet(viewsets.ModelViewSet):
    serializer_class = SupplySerializer
    queryset = Supply.objects.all()
    permission_classes = permissions.IsAuthenticatedOrReadOnly
