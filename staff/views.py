
# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from core.models import Student
from .utils import get_students_for_staff
from hod.models import Course, Attendance


def staff_dashboard(request):
    return render(request, 'core/staff_dashboard.html')

@login_required(login_url="staff_login")
# def mark_attendance(request):
#     students = get_students_for_staff(request.user)

#     for student in students:
#         # student ka course(s) list me le lo (agar multiple courses hain)
#         student_courses[student.id] = student.courses_students.filter(staff=request.user)

#     if request.method == "POST":
#         for student in students:
#             status = request.POST.get(f"attendance_{student.id}")
#             if status:
#                 # Attendance object me course bhi save karo
#                 for course in student_courses[student.id]:
#                     Attendance.objects.create(
#                         student=student,
#                         course=course,
#                         staff=request.user,
#                         status=status
#                     )
#         messages.success(request, "Attendance marked successfully!")
#         return redirect("staff_dashboard")

#     return render(request, "staff/mark_attendance.html", {"students": students, "student_courses": student_courses})

# def mark_attendance(request):
#     students = get_students_for_staff(request.user)

#     if request.method == "POST":
#         for student in students:
#             status = request.POST.get(f"attendance_{student.id}")
#             if status:
#                 Attendance.objects.create(
#                     student=student,
#                     status=status,
#                     marked_by=request.user
#                 )
#         messages.success(request, "Attendance marked successfully!")
#         return redirect("staff_dashboard")

#     return render(request, "staff/mark_attendance.html", {"students": students})

def mark_attendance(request):
    students = get_students_for_staff(request.user)

    if request.method == "POST":
        for student in students:
            # Har student ke liye attendance check karo
            status = request.POST.get(f"attendance_{student.id}")
            if status:
                # Attendance create karo
                Attendance.objects.create(
                    course=student.courses_students.first(),  # agar single course mark karna
                    staff=request.user,
                      # course name as subject
                    date=request.POST.get("date") or None,
                    student=student,
                    status=status
                )
        messages.success(request, "Attendance marked successfully!")
        return redirect("staff_dashboard")

    return render(request, "staff/mark_attendance.html", {"students": students})

# def mark_attendance(request):
#     staff = request.user
#     courses = Course.objects.filter(staff=staff)  # Staff ke courses
#     students = Student.objects.filter(course__in=courses)

#     if request.method == "POST":
#         subject = request.POST.get("subject")
#         course_id = request.POST.get("course")
#         course = Course.objects.get(id=course_id)

#         # 1. HODAttendance create
#         hod_attendance = HODAttendance.objects.create(
#             subject=subject,
#             course=course,
#             staff=staff,
#             date=date.today()
#         )

#         # 2. StudentAttendance create
#         for student in students:
#             status = request.POST.get(f"status_{student.id}")
#             if status:  # present ya absent
#                 StudentAttendance.objects.create(
#                     hod_attendance=hod_attendance,
#                     student=student,
#                     status=status
#                 )

#         messages.success(request, "Attendance marked successfully!")
#         return redirect("mark_attendance")  # page refresh

#     return render(request, "staff/mark_attendance.html", {"students": students, "courses": courses})

# def view_attendance(request):
#     # Staff ke courses
#     courses = Course.objects.filter(staff=request.user)
    
#     # Attendance records un courses ke liye
#     attendance_records = Attendance.objects.filter(course__in=courses).order_by('-date')
    
#     context = {
#         'attendance_records': attendance_records
#     }
#     return render(request, 'hod/view_attendance.html', context)

def view_attendance(request):
    courses = Course.objects.filter(staff=request.user)
    selected_course_id = request.GET.get('course')  # URL me ?course=id
    
    if selected_course_id:
        attendance_records = Attendance.objects.filter(course_id=selected_course_id).order_by('-date')
    else:
        attendance_records = Attendance.objects.filter(course__in=courses).order_by('-date')
    
    context = {
        'attendance_records': attendance_records,
        'courses': courses,
        'selected_course_id': int(selected_course_id) if selected_course_id else None
    }
    return render(request, 'hod/view_attendance.html', context)

    