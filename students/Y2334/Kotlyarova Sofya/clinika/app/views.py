from .models import Service
from .models import Client
from .models import DoctorService
from .models import Doctor
from .models import Ticket

from .serializers import ServiceSerializer
from .serializers import DoctorSerializer
from .serializers import DoctorServiceSerializer
from .serializers import DoctorServicePostSerializer
from .serializers import ClientSerializer
from .serializers import TicketSerializer
from .serializers import TicketPostSerializer

from rest_framework import viewsets
from rest_framework import permissions


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [permissions.AllowAny]


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [permissions.IsAuthenticated]


class DoctorServiceViewSet(viewsets.ModelViewSet):
    queryset = DoctorService.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'update':
            return DoctorServicePostSerializer
        return DoctorServiceSerializer


class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [permissions.IsAuthenticated]


class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'update':
            return TicketPostSerializer
        return TicketSerializer
