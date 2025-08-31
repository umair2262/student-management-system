from django.shortcuts import render
from core.models import Student, Course
from django.contrib.auth.decorators import login_required
from hod.models import Attendance


# Create your views here.
@login_required
def student_dashboard(request):
    return render(request, 'core/student_dashboard.html')

@login_required
def view_attendance(request):
    attendances = Attendance.objects.all().order_by('-date')
    return render(request, "hod/view_attendance.html", {"attendances": attendances})
@login_required
def view_courses(request):
    student = Student.objects.get(user=request.user)  
    courses = [student.course]
    return render(request, "student/view_courses.html", {"courses": courses})

