from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Schedule
from .serializers import SchedulesSerializer


class ScheduleApiView(APIView):
    def get(self, request):
        schedules = Schedule.objects.all()
        serializer = SchedulesSerializer(schedules, many=True)
        return Response({"Schedule": serializer.data})
