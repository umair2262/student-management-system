from django.db import models
from django.conf import settings
from authenticate.models import CustomUser
from core.models import Student
from django.utils import timezone
          # Student model

class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="attendances")
    status = models.CharField(
        max_length=10, 
        choices=(('present', 'Present'), ('absent', 'Absent'))
    )
    marked_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="marked_attendances")
    date = models.DateField(default=timezone.now)  # sirf DateField ke liye default

    def __str__(self):
        return f"{self.student} - {self.status} on {self.date}"