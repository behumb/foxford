from rest_framework import routers
from .views import CourseViewSet, WebinarViewSet, TeacherViewSet, ScheduleViewSet

router = routers.DefaultRouter()

router.register('courses', CourseViewSet, basename='courses')
router.register('webinars', WebinarViewSet, basename='webinars')
router.register('teachers', TeacherViewSet, basename='teachers')
router.register('schedules', ScheduleViewSet, basename='schedules')

urlpatterns = []
urlpatterns += router.urls
