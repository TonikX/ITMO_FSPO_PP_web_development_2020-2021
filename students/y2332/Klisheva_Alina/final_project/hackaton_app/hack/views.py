from datetime import datetime

from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .permissions import *
from .serializer import *
from .models import Issue


def index(request):
    return render(request, 'index.html')


def signup(request):
    return render(request, 'auth/signup.html')


def login(request):
    return render(request, 'auth/login.html')


class UserListAPIView(generics.ListAPIView):
    permission_classes = [IsAdmin]
    serializer_class = UserSerializer
    queryset = User.objects.all()



class TeamListAPIView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TeamSerializer
    queryset = Team.objects.all()


class IssueListAPIView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = IssueSerializer
    queryset = Issue.objects.all()


class SolutionListAPIView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = SolutionSerializer
    queryset = Solution.objects.order_by("pubDate")


class TeamMemberCreateAPIView(generics.CreateAPIView):
    permission_classes = [IsCaptain]
    serializer_class = TeamMemberCreateSerializer
    queryset = TeamMember.objects.all()

class TeamCreateAPIView(generics.CreateAPIView):
    permission_classes = [IsAbstractCaptain]
    serializer_class = TeamCreateSerializer
    queryset = TeamMember.objects.all()


class IssueCreateAPIView(generics.CreateAPIView):
    permission_classes = [IsAdmin]
    serializer_class = IssueGetSerializer
    queryset = Issue.objects.all()


class SolutionCreateAPIView(generics.CreateAPIView):
    permission_classes = [IsAbstractCaptain]
    serializer_class = SolutionCreateSerializer
    queryset = Solution.objects.all()


class TeamMemberGetAPIView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TeamMemberGetSerializer
    queryset = TeamMember.objects.all()


class TeamGetAPIView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TeamGetSerializer
    queryset = Team.objects.all()


class CaptainGetAPIView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CaptainSerializer
    queryset = User.objects.all()


class SolutionGetAPIView(generics.RetrieveAPIView):
    permission_classes = [IsAdmin, IsJury, IsSolutionOwner, IsMentor]
    serializer_class = SolutionGetSerializer
    queryset = Solution.objects.all()


class IssueGetAPIView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = IssueGetSerializer
    queryset = Issue.objects.all()


class TeamMemberUpdateAPIView(generics.UpdateAPIView):
    permission_classes = [IsCaptain]
    serializer_class = TeamMemberCreateSerializer
    queryset = TeamMember.objects.all()


class TeamUpdateAPIView(generics.UpdateAPIView):
    permission_classes = [IsTeamCaptain]
    serializer_class = TeamCreateSerializer
    queryset = Team.objects.all()


class IssueUpdateAPIView(generics.UpdateAPIView):
    permission_classes = [IsAdmin]
    serializer_class = IssueSerializer
    queryset = Issue.objects.all()


class SolutionUpdateAPIView(generics.UpdateAPIView):
    permission_classes = [IsJury]
    serializer_class = SolutionUpdateSerializer
    queryset = Solution.objects.all()


class TeamMemberDeleteAPIView(generics.DestroyAPIView):
    permission_classes = [IsCaptain]
    serializer_class = TeamMemberCreateSerializer
    queryset = TeamMember.objects.all()


class TeamDeleteAPIView(generics.DestroyAPIView):
    permission_classes = [IsCaptain]
    serializer_class = TeamCreateSerializer
    queryset = Team.objects.all()


class IssueDeleteAPIView(generics.DestroyAPIView):
    permission_classes = [IsAdmin]
    serializer_class = IssueSerializer
    queryset = Issue.objects.all()


class SolutionDeleteAPIView(generics.DestroyAPIView):
    permission_classes = [IsSolutionOwner]
    serializer_class = SolutionCreateSerializer
    queryset = Solution.objects.all()
