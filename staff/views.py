
# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import  Attendance
from core.models import Student
from .utils import get_students_for_staff

def staff_dashboard(request):
    return render(request, 'core/staff_dashboard.html')

@login_required(login_url="staff_login")
# def mark_attendance(request):
#     students = Student.objects.all()  # later filter by staff’s class

#     if request.method == "POST":
#         for student in students:
#             status = request.POST.get(f"attendance_{student.id}") # radio button ka name student.id hai
#             if status:
#                 Attendance.objects.create(
#                     student=student,
#                     status=status,
#                     marked_by=request.user
#                 )
#         messages.success(request, "Attendance marked successfully!")
#         return redirect("staff_dashboard")

#     return render(request, "staff/mark_attendance.html", {"students": students})
# def mark_attendance(request):
#     students = Student.objects.all()
#     return render(request, "staff/mark_attendance.html", {"students": students})

def mark_attendance(request):
    students = get_students_for_staff(request.user)

    if request.method == "POST":
        for student in students:
            status = request.POST.get(f"attendance_{student.id}")
            if status:
                Attendance.objects.create(
                    student=student,
                    status=status,
                    marked_by=request.user
                )
        messages.success(request, "Attendance marked successfully!")
        return redirect("staff_dashboard")

    return render(request, "staff/mark_attendance.html", {"students": students})