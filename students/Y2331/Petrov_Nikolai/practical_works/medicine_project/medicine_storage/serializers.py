from django.contrib.auth.models import User
from rest_framework import serializers
from . import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Manufacturer
        fields = ['id', 'name', 'country']


class ActiveSubstanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ActiveSubstance
        fields = ['id', 'name']


class ItemSerializer(serializers.ModelSerializer):
    active_substance = serializers.StringRelatedField()
    packaging = serializers.ChoiceField(choices=models.Item.PackageType.choices, source='get_packaging')
    manufacturer = serializers.StringRelatedField()

    class Meta:
        model = models.Item
        fields = ['id', 'name', 'active_substance', 'packaging', 'manufacturer']


class UnitSerializer(serializers.ModelSerializer):
    item = serializers.StringRelatedField()

    class Meta:
        model = models.Unit
        fields = ['id', 'item', 'amount', 'product_date', 'open_date', 'user']
