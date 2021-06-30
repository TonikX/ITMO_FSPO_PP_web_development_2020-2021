from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from .serialazer import *


class Logout(APIView):

    def get(self, request, format=None):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)


class HostelListView(generics.ListAPIView):
    serializer_class = HostelSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = Hostel.objects.all()
        params = self.request.query_params
        id = params.get('id', None)

        if id:
            queryset = queryset.filter(id=id)
        return queryset


class HostelRetrieveAPIView(RetrieveAPIView):
    serializer_class = HostelSerializers
    queryset = Hostel.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class RoomListView(generics.ListAPIView):
    serializer_class = RoomSerializer

    def get_queryset(self):
        queryset = Room.objects.all()
        params = self.request.query_params
        id = params.get('id', None)
        hostel = params.get('hostel_id', None)

        if id:
            queryset = queryset.filter(id=id)

        if hostel:
            queryset = queryset.filter(hostel_id=hostel)

        return queryset


class PaymentListView(generics.ListAPIView):
    # queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get_queryset(self):
        queryset = Payment.objects.all()
        params = self.request.query_params
        checkin = params.get('check_in_out_id', None)
        resident = params.get('resident_id', None)

        if checkin:
            queryset = queryset.filter(check_in_out_id=checkin)
        if resident:
            queryset = queryset.filter(check_in_out_id__resident_id=resident)
        return queryset


class PaymentCreateAPIView(generics.CreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentCreateSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class PaymentUpdate(generics.RetrieveUpdateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentCreateSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class PaymentsRetrieveView(generics.RetrieveAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentCreateSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CheckInListView(generics.ListAPIView):
    serializer_class = CheckInSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = Check_in_out.objects.all()
        params = self.request.query_params
        resident = params.get('resident_id', None)
        room = params.get('room_id', None)
        comment = params.get('comment', None)

        if resident:
            queryset = queryset.filter(resident_id=resident)

        if room:
            queryset = queryset.filter(room_id=room)

        if comment:
            queryset = queryset.filter(comment=comment)
        return queryset


class CheckinUpdate(generics.RetrieveUpdateAPIView):
    serializer_class = CheckinCreateSerializer
    queryset = Check_in_out.objects.all()
    permission_classes = [permissions.IsAdminUser]


class CheckinDelete(generics.RetrieveDestroyAPIView):
    serializer_class = CheckinCreateSerializer
    queryset = Check_in_out.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CheckInCreate(generics.CreateAPIView):
    queryset = Check_in_out.objects.all()
    serializer_class = CheckinCreateSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CheckUpdate(generics.RetrieveUpdateAPIView):
    queryset = Check_in_out.objects.all()
    serializer_class = CheckinCreateSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ResidentList(generics.ListAPIView):
    serializer_class = ResidentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = Resident.objects.all()
        params = self.request.query_params
        return queryset


class ResidentCreateView(generics.CreateAPIView):
    queryset = Resident.objects.all()
    serializer_class = ResidentCreateSerializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer_class):
        instance = serializer_class.save()
        instance.set_password(instance.password)
        instance.save()


class ResidentUpdate(generics.RetrieveUpdateAPIView):
    queryset = Resident.objects.all()
    serializer_class = ResidentCreateSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ResidentRetrive(generics.RetrieveAPIView):
    queryset = Resident.objects.all()
    serializer_class = ResidentCreateSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class RoomUpdate(generics.RetrieveUpdateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomCreateSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

