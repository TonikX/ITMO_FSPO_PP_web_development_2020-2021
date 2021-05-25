from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()

router.register('disciplines', DisciplineViewSet, basename='discipline')
router.register('lecturers', LecturerViewSet, basename='lecturer')
router.register('groups', GroupViewSet, basename='group')
router.register('audiences', AudienceViewSet, basename='audiences')
router.register('schedules', ScheduleViewSet, basename='schedule')

urlpatterns = router.urls
