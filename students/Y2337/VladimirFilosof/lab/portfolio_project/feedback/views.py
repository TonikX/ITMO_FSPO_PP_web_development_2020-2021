from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework.viewsets import ModelViewSet

from feedback.models import Feedback
from feedback.permissions import IsAuthenticatedOwnerOrReadOnly
from feedback.serializers import FeedbackSerializer, FeedbackCreateSerializer, FeedbackPatchSerializer


class FeedbackViewSet(ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    permission_classes = [IsAuthenticatedOwnerOrReadOnly]
    filter_fields = ['id']

    def perform_create(self, serializer):
        serializer.validated_data['user'] = self.request.user
        serializer.save(user=self.request.user)
    #
    # def list(self, request, *args, **kwargs):
    #     queryset = Feedback.objects.all()
    #     serializer = FeedbackSerializer(queryset)
    #     data = serializer.data
    #     if data['user'] == request.user:
    #         print(request.user)


class FeedbackAPIView(APIView):
    permission_classes = [IsAuthenticatedOwnerOrReadOnly]

    def get(self, request):
        feedbacks = Feedback.objects.all()
        serializer = FeedbackSerializer(feedbacks, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FeedbackCreateSerializer(data=request.data)
        serializer.is_valid()
        serializer.validated_data['user'] = request.user

        serializer.save()
        return Response(serializer.data)


class ServiceFeedbackAPIView(APIView):
    permission_classes = [IsAuthenticatedOwnerOrReadOnly]

    def get(self, request, service_id):
        feedbacks = Feedback.objects.filter(service=service_id)

        serializer = FeedbackSerializer(feedbacks, many=True).data
        for feedback in serializer:
            feedback['owner'] = (feedback['user'] == request.user.id)
        return Response(serializer)


class FeedbackDetailAPIView(APIView):
    permission_classes = [IsAuthenticatedOwnerOrReadOnly]

    def delete(self, request, pk):
        feedback = Feedback.objects.get(pk=pk)
        feedback.delete()
        return Response()

    def patch(self, request, pk):
        feedback = Feedback.objects.get(pk=pk)

        serializer = FeedbackPatchSerializer(feedback, data=request.data)
        serializer.is_valid()

        serializer.save()
        return Response(serializer.data)
