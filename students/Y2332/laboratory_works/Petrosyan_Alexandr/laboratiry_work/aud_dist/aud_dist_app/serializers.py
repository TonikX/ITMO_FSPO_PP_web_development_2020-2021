from rest_framework import serializers

from .models import *


class AudienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Audience
        fields = ("number",)


class LecturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecturer
        fields = ("surname", "firstname", "patronymic")


class DisciplineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discipline
        fields = ("name",)


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ("number",)


class SchedulesSerializer(serializers.ModelSerializer):
    discipline = DisciplineSerializer()
    audience = AudienceSerializer()
    lecturer = LecturerSerializer()
    group = GroupSerializer()

    class Meta:
        model = Schedule
        fields = (
            "discipline",
            "lecturer",
            "audience",
            "group",
            "day_of_the_week",
            "begin_time"
        )
