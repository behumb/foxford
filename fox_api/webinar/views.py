from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .serializers import CourseSerializer, CourseDitailSerializer, WebinarSerializer, TeacherSerializer, \
    ScheduleSerializer, CourseShortSerializer, WebinarShortSerializer, WebinarDitailSerializer, TeacherDitailSerializer, \
    ScheduleDitailSerializer, SalaryRequestSerializer
from .models import Course, Schedule, Teacher, Webinar
from .services import get_month_salary


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_classes = {
        'list': CourseShortSerializer,
        'retrieve': CourseDitailSerializer,
    }
    default_serializer_class = CourseSerializer

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)


class WebinarViewSet(ModelViewSet):
    queryset = Webinar.objects.prefetch_related('teachers')
    serializer_classes = {
        'list': WebinarShortSerializer,
        'retrieve': WebinarDitailSerializer,
    }
    default_serializer_class = WebinarSerializer

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)


class TeacherViewSet(ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_classes = {
        'retrieve': TeacherDitailSerializer,
        'salary': SalaryRequestSerializer
    }
    default_serializer_class = TeacherSerializer

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)

    @action(methods=['post'], detail=True)
    def salary(self, request, pk):
        month_serializer = self.get_serializer(data=request.data)
        if month_serializer.is_valid():
            salary = get_month_salary(teacher=self.get_object(),
                                      mount=month_serializer.validated_data['month'])
            return Response(salary)
        return Response(data={'error': 'Invalid month format (it must be YYYY-mm)'},
                        status=status.HTTP_400_BAD_REQUEST)


class ScheduleViewSet(ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_classes = {
        'list': ScheduleDitailSerializer,
        'retrieve': ScheduleDitailSerializer,
    }
    default_serializer_class = ScheduleSerializer

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)
