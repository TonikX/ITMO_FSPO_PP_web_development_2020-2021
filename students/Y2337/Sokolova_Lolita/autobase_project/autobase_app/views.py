from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from autobase_app.models import Driver, MotorDepot, Garage, Car, Fuel, Waybill, Refuel
from autobase_app.serializer import DriverSerializer, MotorDepotSerializer, GarageSerializer, \
    CarSerializer, FuelSerializer, WaybillSerializer, RefuelSerializer


class DriverViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer


class MotorDepotViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = MotorDepot.objects.all()
    serializer_class = MotorDepotSerializer


class GarageViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Garage.objects.all()
    serializer_class = GarageSerializer


class CarViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class FuelViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Fuel.objects.all()
    serializer_class = FuelSerializer


class WaybillAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        queryset = Waybill.objects.all()
        serializer = WaybillSerializer(queryset, many=True).data

        print(serializer)

        for item in serializer:
            if item['id_car']:
                item['car_number'] = Car.objects.get(pk=item['id_car']).reg_number
            else:
                item['car_number'] = "Такой машины больше нет"
            if item['id_driver']:
                item['driver_name'] = Driver.objects.get(pk=item['id_driver']).name
            else:
                item['driver_name'] = "Такого водителя больше нет"



        return Response(serializer)

    def post(self, request):
        serializer = WaybillSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)


class WaybillDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        item = Waybill.objects.get(pk=pk)
        serializer = WaybillSerializer(item).data

        print(serializer)

        return Response(serializer)

    def put(self, request, pk):
        item = Waybill.objects.get(pk=pk)
        serializer = WaybillSerializer(item, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)

    def delete(self, request, pk):
        item = Waybill.objects.get(pk=pk)
        item.delete()

        return Response()


class RefuelAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        queryset = Refuel.objects.all()
        serializer = RefuelSerializer(queryset, many=True).data

        print(serializer)

        for item in serializer:
            if item['car_id']:
                item['car_number'] = Car.objects.get(pk=item['car_id']).reg_number
            else:
                item['car_number'] = "Такой машины больше нет"
            if item['id_fuel']:
                item['fuel_name'] = Fuel.objects.get(pk=item['id_fuel']).fuel_name
            else:
                item['fuel_name'] = "Такого топлива больше нет"

        return Response(serializer)

    def post(self, request):
        serializer = RefuelSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)


class RefuelDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        item = Refuel.objects.get(pk=pk)
        serializer = RefuelSerializer(item).data

        print(serializer)

        return Response(serializer)

    def put(self, request, pk):
        item = Refuel.objects.get(pk=pk)
        serializer = RefuelSerializer(item, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)

    def delete(self, request, pk):
        item = Refuel.objects.get(pk=pk)
        item.delete()

        return Response()
