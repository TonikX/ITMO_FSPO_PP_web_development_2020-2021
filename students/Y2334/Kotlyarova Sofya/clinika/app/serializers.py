from .models import Service
from .models import Client
from .models import Doctor
from .models import DoctorService
from .models import Ticket
from rest_framework import serializers


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ('id', 'name')


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('id', 'name', 'phone', 'document_number')


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ('id', 'name', 'phone', 'speciality')


class DoctorNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ('id', 'name')


class DoctorServiceSerializer(serializers.ModelSerializer):
    doctor = DoctorNameSerializer()
    service = ServiceSerializer()

    class Meta:
        model = DoctorService
        fields = ('id', 'doctor', 'service', 'price')


class DoctorServicePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorService
        fields = ('id', 'doctor', 'service', 'price')


class ClientTicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('id', 'name')


class TicketSerializer(serializers.ModelSerializer):
    client = ClientTicketSerializer()
    doctor_service = DoctorServiceSerializer()

    class Meta:
        model = Ticket
        fields = ('id', 'client', 'doctor_service', 'when')


class TicketPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ('id', 'client', 'doctor_service', 'when')
