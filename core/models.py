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
    hod = models.ForeignKey(HOD, on_delete=models.CASCADE, related_name="staffs")  
    full_name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name

class Course(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20, unique=True)
    hod = models.ForeignKey(HOD, on_delete=models.CASCADE, related_name="courses")  


    def __str__(self):
        return self.name


# Student model
class Student(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="student_profile")
    roll_no = models.CharField(max_length=50, unique=True, null=True, blank=True)
    hod = models.ForeignKey(HOD, on_delete=models.CASCADE, related_name="students")  
    # course = models.CharField(max_length=100, null=True, blank=True)
    course = models.ManyToManyField("Course", related_name="students", blank=True)  
    created_at = models.DateTimeField(auto_now_add=True)
    # hod = models.ForeignKey(HOD, on_delete=models.CASCADE, related_name="students",)  
    hod = models.ForeignKey(
        HOD,
        on_delete=models.CASCADE,
        related_name="students",
        null=True,       # allows NULL in DB
        blank=True       # allows empty in forms/admin
    )  

   
    
    def __str__(self):
        full_name = self.user.get_full_name()
        return f"{full_name or self.user.username} ({self.roll_no})"


