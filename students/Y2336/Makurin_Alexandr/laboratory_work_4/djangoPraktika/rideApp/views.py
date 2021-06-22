from rest_framework import viewsets, status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Playground, Ride, Usage
from .serializers import PlaygroundSerializer, RideSerializer, UsageSerializer


class PlaygroundViewSet(viewsets.ModelViewSet):
    serializer_class = PlaygroundSerializer
    queryset = Playground.objects.all()
    permission_classes = permissions.IsAuthenticatedOrReadOnly,


class RideViewSet(viewsets.ModelViewSet):
    serializer_class = RideSerializer
    queryset = Ride.objects.all()
    permission_classes = permissions.IsAuthenticatedOrReadOnly,


class UsageViewSet(viewsets.ModelViewSet):
    serializer_class = UsageSerializer
    queryset = Usage.objects.all()


class Logout(APIView):

    def get(self, request, format=None):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)
