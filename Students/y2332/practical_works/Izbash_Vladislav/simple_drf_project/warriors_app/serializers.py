from rest_framework import serializers
from .models import Skill, Warrior


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'


class WarriorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warrior
        fields = '__all__'


class WarriorProfSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warrior
        exclude = ['skill']


class WarriorSkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warrior
        exclude = ['profession']


# class WarriorSkillsSerializer(WarriorSerializer):
#     skills = serializers.SerializerMethodField('get_skills')
#
#     def get_skills(self, warrior):
#         warrior.skill.all()
#         # skills = warrior.skillofwarrior_set().all()
