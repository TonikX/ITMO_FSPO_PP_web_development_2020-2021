from rest_framework import serializers
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from .models import Ride, Playground, Usage


class RideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ride
        fields = ('id', 'name', 'startDate', 'lifetime', 'basePrice', 'playground')


class PlaygroundSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playground
        fields = ('id', 'address', 'directorSurname', 'childrenPrice', 'discountPrice', 'adultPrice')


class UsageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usage
        fields = ('id', 'day', 'ride', 'childrenSales', 'discountSales', 'adultSales')
