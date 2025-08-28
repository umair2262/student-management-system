# # from django import forms
# # from django.contrib.auth.forms import UserCreationForm
# # from django.contrib.auth.models import User
# # from .models import HOD, Staff

# # # HOD User Form
# # class HodUserForm(UserCreationForm):
# #     password1 = forms.CharField(widget=forms.PasswordInput)
# #     password2 = forms.CharField(widget=forms.PasswordInput)

# #     class Meta:
# #         model = User
# #         fields = ['username', 'email', 'password1', 'password2']

# # # HOD Profile Form
# # class HodProfileForm(forms.ModelForm):
# #     class Meta:
# #         model = HOD
# #         fields = ['department', 'phone', 'address']

# # # Staff User Form
# # class StaffUserForm(UserCreationForm):
# #     password1 = forms.CharField(widget=forms.PasswordInput)
# #     password2 = forms.CharField(widget=forms.PasswordInput)

# #     class Meta:
# #         model = User
# #         fields = ['username', 'email', 'password1', 'password2']

# # # Staff Profile Form
# # class StaffProfileForm(forms.ModelForm):
# #     class Meta:
# #         model = Staff
# #         fields = ['department', 'phone', 'address']

# from django import forms
# from .models import Course, Notification

# class AssignCourseForm(forms.ModelForm):
#     class Meta:
#         model = Course
#         fields = ['name', 'staff', 'students']
#         widgets = {
#             'students': forms.CheckboxSelectMultiple
#         }

# class NotificationForm(forms.ModelForm):
#     class Meta:
#         model = Notification
#         fields = ['title', 'message', 'recipient_role']
from django import forms
from .models import Course
from authenticate.models import CustomUser
from .models import Attendance

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'code', 'staff', 'students']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'code': forms.TextInput(attrs={'class': 'form-control'}),
            'staff': forms.Select(attrs={'class': 'form-control'}),
            'students': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['staff'].queryset = CustomUser.objects.filter(role='STAFF')
        self.fields['students'].queryset = CustomUser.objects.filter(role='STUDENT')


class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['subject', 'staff']
