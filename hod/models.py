from django.db import models
from authenticate.models import CustomUser

class Course(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20)
    staff = models.ForeignKey(CustomUser, limit_choices_to={'role': 'STAFF'}, on_delete=models.SET_NULL, null=True, related_name='courses_staff')
    students = models.ManyToManyField(CustomUser, limit_choices_to={'role': 'STUDENT'}, blank=True, related_name='courses_students')

    def __str__(self):
        return self.name

from datetime import date

class Attendance(models.Model):
    subject = models.CharField(max_length=50)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    staff = models.ForeignKey(CustomUser, on_delete=models.CASCADE, limit_choices_to={'role': 'STAFF'}, related_name='hod_attendance')
    date = models.DateField(default=date.today)

    def __str__(self):
        return f"{self.subject} - {self.staff.username} - {self.date}"

class AttendanceReport(models.Model):
    student = models.ForeignKey(CustomUser, on_delete=models.CASCADE, limit_choices_to={'role': 'STUDENT'})
    attendance = models.ForeignKey(Attendance, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)  # Present=True, Absent=False

    def __str__(self):
        return f"{self.student.username} - {self.attendance.subject} - {'Present' if self.status else 'Absent'}"

class Subject(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20)
    # aur bhi fields

    def __str__(self):
        return self.name