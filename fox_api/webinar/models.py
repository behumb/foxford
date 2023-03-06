from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name


class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    bio = models.TextField()
    webinars = models.ManyToManyField('Webinar', through='Schedule', through_fields=('teacher', 'webinar'))

    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.middle_name}'

    def get_full_name(self):
        return f'{self.last_name} {self.first_name} {self.middle_name}'


class Webinar(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='webinars')
    rate = models.FloatField()
    teachers = models.ManyToManyField('Teacher', through='Schedule', through_fields=('webinar', 'teacher'))

    def __str__(self):
        return self.title


class Schedule(models.Model):
    STATUS_CHOICES = (
        ('created', 'Created'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('canceled', 'Canceled')
    )
    start_time = models.DateTimeField()
    duration = models.PositiveIntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='created')
    webinar = models.ForeignKey(Webinar, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return
