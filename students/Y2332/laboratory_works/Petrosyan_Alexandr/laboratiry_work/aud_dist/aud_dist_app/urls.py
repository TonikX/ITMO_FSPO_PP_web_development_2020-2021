from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()

router.register('directions', DirectionViewSet, basename='direction')
router.register('syllabuses', SyllabusViewSet, basename='syllabus')
router.register('disciplines', DisciplineViewSet, basename='discipline')
router.register('lecturers', LecturerViewSet, basename='lecturer')
router.register('groups', GroupViewSet, basename='group')
router.register('classrooms', ClassroomViewSet, basename='classroom')
router.register('schedules', ScheduleViewSet, basename='schedule')

urlpatterns = router.urls
