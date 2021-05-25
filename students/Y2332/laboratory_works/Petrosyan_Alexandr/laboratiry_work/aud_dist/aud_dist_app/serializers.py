from rest_framework import serializers

from .models import *


class DisciplineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discipline
        fields = '__all__'


class LecturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecturer
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class AudienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Audience
        fields = '__all__'


class SchedulesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = '__all__'
