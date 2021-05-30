from rest_framework.serializers import *
from .models import *


class BodySerializer(ModelSerializer):
    class Meta:
        model = Body
        fields = '__all__'


class EngineSerializer(ModelSerializer):
    class Meta:
        model = Engine
        fields = '__all__'


class CarModelSerializer(ModelSerializer):
    class Meta:
        model = CarModel
        fields = '__all__'


class LegalOwnerSerializer(ModelSerializer):
    class Meta:
        model = LegalOwner
        fields = '__all__'


class PhysicalOwnerSerializer(ModelSerializer):
    class Meta:
        model = PhysicalOwner
        fields = '__all__'


class CarSerializer(ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'


class DriveAwayInfoSerializer(ModelSerializer):
    class Meta:
        model = DriveAwayInfo
        fields = '__all__'


class InspectorSerializer(ModelSerializer):
    class Meta:
        model = Inspector
        fields = '__all__'


class WatchInfoSerializer(ModelSerializer):
    class Meta:
        model = WatchInfo
        fields = '__all__'