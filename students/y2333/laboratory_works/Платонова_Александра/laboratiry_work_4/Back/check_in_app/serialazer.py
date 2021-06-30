from abc import ABCMeta

from rest_framework import serializers
from .models import *


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = "__all__"


class OrgSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organizatoin
        fields = "__all__"


class ResidentSerializer(serializers.ModelSerializer):
    organization_id = OrgSerializer(many=False)

    class Meta:
        model = Resident
        fields = "__all__"


class HostelSerializers(serializers.ModelSerializer):
    address_id = AddressSerializer(many=False)

    class Meta:
        model = Hostel
        fields = "__all__"


class RoomSerializer(serializers.ModelSerializer):
    hostel_id = HostelSerializers(many=False)

    class Meta:
        model = Room
        fields = "__all__"


class RoomCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = "__all__"


class CheckInSerializer(serializers.ModelSerializer):
    resident_id = ResidentSerializer(many=False)
    room_id = RoomSerializer(many=False)

    class Meta:
        model = Check_in_out
        fields = "__all__"


class CheckinCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Check_in_out
        fields = "__all__"


class PaymentSerializer(serializers.ModelSerializer):
    check_in_out_id = CheckInSerializer(many=False)

    class Meta:
        model = Payment
        fields = "__all__"


class ResidentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resident
        fields = "__all__"


class PaymentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"
# class PaymentCreateSerializer(serializers.Serializer):
#     amount = serializers.FloatField(validators=[MinValueValidator(0)])
#     status = serializers.CharField(max_length=50)
#     date_pay = serializers.DateField(default=date.today)
#     check_in_out_id = models.ForeignKey(Check_in_out, on_delete=models.CASCADE, default=1)
#
#     def create(self, validated_data):
#         return Payment(**validated_data)
