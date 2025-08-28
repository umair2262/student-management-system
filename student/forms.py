from django import forms
from core.models import Student

class StudentForm(forms.ModelForm):
    username = forms.CharField(max_length=150, required=True)
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=False)

    class Meta:
        model = Student
        fields = ['roll_no', 'course', 'username', 'email', 'password']

    def save(self, commit=True):
        student = super().save(commit=False)
        user = student.user
        user.username = self.cleaned_data['username']
        user.email = self.cleaned_data['email']
        if self.cleaned_data['password']:
            user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
            student.save()
        return student
