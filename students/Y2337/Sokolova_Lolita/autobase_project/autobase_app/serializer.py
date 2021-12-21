from rest_framework.serializers import ModelSerializer

from autobase_app.models import Car, Driver, MotorDepot, Garage, Fuel, Waybill, Refuel


class CarSerializer(ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'


class DriverSerializer(ModelSerializer):
    class Meta:
        model = Driver
        fields = '__all__'


class MotorDepotSerializer(ModelSerializer):
    class Meta:
        model = MotorDepot
        fields = '__all__'


class GarageSerializer(ModelSerializer):
    class Meta:
        model = Garage
        fields = '__all__'


class FuelSerializer(ModelSerializer):
    class Meta:
        model = Fuel
        fields = '__all__'


class WaybillSerializer(ModelSerializer):
    class Meta:
        model = Waybill
        fields = '__all__'


class RefuelSerializer(ModelSerializer):
    class Meta:
        model = Refuel
        fields = '__all__'

