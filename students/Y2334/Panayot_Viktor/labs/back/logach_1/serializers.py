from django.db.models import fields
from rest_framework import serializers
from .models import *

class LogikSerializer(serializers.ModelSerializer):
    class Meta:
        model = Logik
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class LogikTaskSerializer(serializers.ModelSerializer):
    logik = LogikSerializer()
    
    class Meta:
        model = LogikTask
        fields = '__all__'

class UpdateLogikTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = LogikTask
        fields = '__all__'