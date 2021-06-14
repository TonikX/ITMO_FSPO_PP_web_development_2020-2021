from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from order.models import Service, Order
from order.permissions import IsStaffOrReadOnly, IsAuthenticatedOwner
from order.serializers import ServiceSerializer, OrderSerializer, UserSerializer


class ServiceViewSet(ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    filter_backends = [SearchFilter]
    permission_classes = [IsStaffOrReadOnly]


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = [SearchFilter]
    permission_classes = [IsAuthenticatedOwner]
    filter_fields = ['id']

    def perform_create(self, serializer):
        serializer.validated_data['user'] = self.request.user
        serializer.save(user=self.request.user)


class OrderServiceAPIView(APIView):
    def get(self, request):
        queryset = request.user.orders.all()
        serializer_data = ServiceSerializer(queryset, many=True).data
        return Response(serializer_data)


class UsernameAPIView(APIView):
    def patch(self, request):
        request.user.first_name = request.data['first_name']
        request.user.last_name = request.data['last_name']
        request.user.save()
        return Response({
            'first_name': request.user.first_name,
            'last_name': request.user.last_name
        })

    def get(self, request):
        serializer_data = UserSerializer(request.user)
        return Response(serializer_data)
