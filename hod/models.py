from django.db import models
from authenticate.models import CustomUser
from datetime import date


class Course(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20)
    staff = models.ForeignKey(CustomUser, limit_choices_to={'role': 'STAFF'}, on_delete=models.SET_NULL, null=True, related_name='courses_staff')
    students = models.ManyToManyField(CustomUser, limit_choices_to={'role': 'STUDENT'}, blank=True, related_name='courses_students')

    def __str__(self):
        return self.name


class Attendance(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        limit_choices_to={'role': 'STUDENT'},
        related_name="attendance_student"
    )
    staff = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        limit_choices_to={'role': 'STAFF'},
        related_name="attendance_staff"
    )
    date = models.DateField(auto_now_add=True)

    STATUS_CHOICES = (
        ('Present', 'Present'),
        ('Absent', 'Absent'),
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    def __str__(self):
        return f"{self.student.username} - {self.course.name} - {self.date}"
