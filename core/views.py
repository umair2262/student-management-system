# 
from django.shortcuts import render
from authenticate.decorators import allowed_users
from django.contrib.auth.decorators import login_required

def home_view(request):
    return render(request, 'base.html')

def home(request):
    return render(request, 'core/home.html')

@login_required
@allowed_users(allowed_roles=['HOD'])
def hod_dashboard(request):
    return render(request, 'core/hod_dashboard.html')

@login_required
@allowed_users(allowed_roles=['Staff'])
def staff_dashboard(request):
    return render(request, 'core/staff_dashboard.html')

@login_required
@allowed_users(allowed_roles=['Student'])
def student_dashboard(request):
    return render(request, 'core/student_dashboard.html')


