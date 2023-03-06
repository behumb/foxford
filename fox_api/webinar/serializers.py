from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField, Serializer, DateField
from .models import Course, Webinar, Teacher, Schedule


class TeacherShortSerializer(ModelSerializer):
    class Meta:
        model = Teacher
        fields = ('id', 'get_full_name')


class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'name', 'description')


class WebinarSerializer(ModelSerializer):
    course = PrimaryKeyRelatedField(queryset=Course.objects.all())

    class Meta:
        model = Webinar
        fields = ('id', 'title', 'description', 'rate', 'course')


class CourseShortSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'name')


class WebinarShortSerializer(ModelSerializer):
    course = CourseShortSerializer()

    class Meta:
        model = Webinar
        fields = ('id', 'title', 'course')


class CourseDitailSerializer(ModelSerializer):
    webinars = WebinarShortSerializer(many=True)

    class Meta:
        model = Course
        fields = ('id', 'name', 'description', 'webinars')


class ScheduleSerializer(ModelSerializer):
    teacher = PrimaryKeyRelatedField(queryset=Teacher.objects.all())
    webinar = PrimaryKeyRelatedField(queryset=Webinar.objects.all())

    class Meta:
        model = Schedule
        fields = ('id', 'start_time', 'duration', 'teacher', 'webinar')


class ScheduleDitailSerializer(ModelSerializer):
    teacher = TeacherShortSerializer()
    webinar = WebinarShortSerializer()

    class Meta:
        model = Schedule
        fields = ('id', 'start_time', 'duration', 'teacher', 'webinar')


class TeacherSerializer(ModelSerializer):
    class Meta:
        model = Teacher
        fields = ('id', 'first_name', 'last_name', 'middle_name', 'bio', 'email')


class TeacherDitailSerializer(ModelSerializer):
    webinars = WebinarShortSerializer(many=True)

    class Meta:
        model = Teacher
        fields = ('id', 'first_name', 'last_name', 'middle_name', 'bio', 'email', 'webinars')


class WebinarDitailSerializer(ModelSerializer):
    course = CourseShortSerializer()
    teachers = TeacherShortSerializer(many=True)

    class Meta:
        model = Webinar
        fields = ('id', 'title', 'description', 'rate', 'course', 'teachers')


class SalaryRequestSerializer(Serializer):
    month = DateField(format='%Y-%m', input_formats=['%Y-%m'])
