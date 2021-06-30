from rest_framework import serializers, fields
from .models import *


class UserSerializer(serializers.ModelSerializer):
    role = serializers.CharField(source="get_role_display", read_only=True)

    class Meta:
        model = User
        fields = ["id","username", "email", "role", "first_name", "last_name", "phoneNumber"]


class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = "__all__"


class SolutionBaseSerializer(serializers.ModelSerializer):
    jury = UserSerializer()
    issue = IssueSerializer()
    class Meta:
        model = Solution
        fields = "__all__"


class TeamSerializer(serializers.ModelSerializer):
    solutions = SolutionBaseSerializer(many=True, read_only=True)
    captain = UserSerializer()

    class Meta:
        model = Team
        fields = "__all__"

class TeamBaseSerializer(serializers.ModelSerializer):
    captain = UserSerializer()
    class Meta:
        model = Team
        fields = "__all__"

class SolutionSerializer(serializers.ModelSerializer):
    team = TeamBaseSerializer()
    jury = UserSerializer()

    class Meta:
        model = Solution
        fields = "__all__"


class TeamMemberSerializer(serializers.ModelSerializer):
    role = serializers.CharField(source="get_role_display", read_only=True)

    class Meta:
        model = TeamMember
        fields = "__all__"


class SolutionGetSerializer(serializers.ModelSerializer):
    team = TeamSerializer()
    jury = UserSerializer()

    class Meta:
        model = Solution
        fields = "__all__"


class TeamGetSerializer(serializers.ModelSerializer):
    captain = UserSerializer()
    team_members = TeamMemberSerializer(many=True, read_only=True)
    solutions = SolutionBaseSerializer(many=True, read_only=True)

    class Meta:
        model = Team
        fields = "__all__"


class CaptainSerializer(serializers.ModelSerializer):
    team = TeamGetSerializer(read_only=True)

    class Meta:
        model = User
        fields = ["username", "team"]


class TeamMemberGetSerializer(serializers.ModelSerializer):
    role = serializers.CharField(source="get_role_display", read_only=True)
    team = TeamSerializer()

    class Meta:
        model = TeamMember
        fields = "__all__"


class IssueGetSerializer(serializers.ModelSerializer):
    dateCreate = fields.DateField(input_formats=['%d.%m.%Y'])
    solutions = SolutionSerializer(many=True, read_only=True)

    class Meta:
        model = Issue
        fields = "__all__"


class TeamCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = "__all__"


class TeamMemberCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMember
        fields = "__all__"


class SolutionCreateSerializer(serializers.ModelSerializer):

    pubDate = fields.DateField(input_formats=['%d.%m.%Y'])
    class Meta:
        model = Solution
        fields = "__all__"


class SolutionUpdateSerializer(serializers.ModelSerializer):
    checkDate = fields.DateField(input_formats=['%d.%m.%Y'])

    class Meta:
        model = Solution
        fields = "__all__"