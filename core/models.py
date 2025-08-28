from django.db import models
from django.conf import settings



# HOD model
class HOD(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="hod_profile")
    full_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name


# Staff model
class Staff(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="staff_profile")
    full_name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name

class Course(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Student model
class Student(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="student_profile")
    roll_no = models.CharField(max_length=50, unique=True, null=True, blank=True)
    course = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
   
    # def __str__(self): 
    #     return f"{self.user.get_full_name} ({self.roll_no})"
    def __str__(self):
        full_name = self.user.get_full_name()
        return f"{full_name or self.user.username} ({self.roll_no})"


