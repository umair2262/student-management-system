# from django import forms
# from authenticate.models import CustomUser
# from .models import Staff  # Staff model import

# class StaffForm(forms.ModelForm):
#     email = forms.EmailField(required=True)
#     password = forms.CharField(widget=forms.PasswordInput)

#     class Meta:
#         model = Staff
#         fields = ['address']  # Staff ke extra fields

#     def save(self, commit=True):
#         user = CustomUser.objects.create_user(
#             username=self.cleaned_data['email'],
#             email=self.cleaned_data['email'],
#             password=self.cleaned_data['password'],
#             user_type=2  # staff
#         )
#         staff = Staff.objects.create(
#             admin=user,
#             address=self.cleaned_data['address']
#         )
#         return staff


from django import forms
from core.models import Staff  # ab core se Staff import kar rahe hain

class StaffForm(forms.Form):
    username = forms.CharField(max_length=150)
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    

