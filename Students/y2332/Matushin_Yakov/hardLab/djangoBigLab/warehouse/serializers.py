from rest_framework import serializers
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from .models import Employer, Client, Supplier, Production, Batch


class EmployerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employer
        fields = ('id', 'code', 'name', 'pass_data')


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('id', 'name', 'acc_num')


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ('id', 'name', 'address')


class ProductionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Production
        fields = ('id', 'code', 'name', 'unit', 'amount', 'minimum', 'desc')


class BatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Batch
        fields = ('id', 'supplier', 'client', 'employer', 'production', 'supply_date', 'delivery_date', 'amount', 'price', 'isFulfilled')