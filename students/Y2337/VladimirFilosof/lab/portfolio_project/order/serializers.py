from rest_framework.serializers import ModelSerializer

from order.models import Order, Service, User


class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class ServiceSerializer(ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']
