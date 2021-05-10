from rest_framework import generics

from .serializers import *


# Create your views here.


class SkillList(generics.ListAPIView):
    serializer_class = SkillSerializer
    queryset = Skill.objects.all()


class SkillCreate(generics.CreateAPIView):
    serializer_class = SkillSerializer
    queryset = Skill.objects.all()


class WarriorProfList(generics.ListAPIView):
    serializer_class = WarriorProfSerializer
    queryset = Warrior.objects.all()


class WarriorSkillsList(generics.ListAPIView):
    serializer_class = WarriorSkillsSerializer
    queryset = Warrior.objects.all()


class WarriorGet(generics.RetrieveAPIView):
    serializer_class = WarriorSerializer
    queryset = Warrior.objects.all()


class WarriorDelete(generics.DestroyAPIView):
    queryset = Warrior.objects.all()


class WarriorUpdate(generics.UpdateAPIView):
    serializer_class = WarriorSerializer
    queryset = Warrior.objects.all()

