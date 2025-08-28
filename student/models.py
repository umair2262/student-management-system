

# # Create your models here.
# from django.db import models
# from authenticate.models import CustomUser

# class Student(models.Model):
#     user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
#     full_name = models.CharField(max_length=100)
#     roll_number = models.CharField(max_length=50)
#     course = models.CharField(max_length=100)
#     enrollment_number = models.CharField(max_length=50)  # agar tumne add karna hai
#     address = models.TextField(blank=True, null=True)

#     def __str__(self):
#         return self.full_name
