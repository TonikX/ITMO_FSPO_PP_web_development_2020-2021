from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from order.permissions import IsStaffOrReadOnly
from projects.models import Project
from projects.serializers import ProjectSerializer


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    permission_classes = [IsStaffOrReadOnly]
    filter_fields = ['id']
    search_fields = ['title', 'description']
