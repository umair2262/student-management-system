from django import forms
from .models import HOD, Staff, Student

class HODForm(forms.ModelForm):
    class Meta:
        model = HOD
        fields = ['user', 'full_name']

class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ['user', 'full_name', 'department']

class StudentForm(forms.ModelForm):
    
    class Meta:
        model = Student
        fields = ['username', 'full_name', 'department']

