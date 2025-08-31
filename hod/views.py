from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# from .forms import StaffUserForm, StaffProfileForm
from django.shortcuts import render, redirect, get_object_or_404
from staff.forms import StaffForm 
from student.forms import StudentForm 

from django.utils.crypto import get_random_string #ye random password kelia ha 
from authenticate.models import CustomUser
from core.models import Staff, Student
from django.contrib.auth import get_user_model
from django.template.loader import get_template



# HOD login view
def hod_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('hod_dashboard')
        else:
            messages.error(request, "Invalid username or password")
            return redirect('hod_login')
    return render(request, 'auth/login.html')

# HOD dashboard view
@login_required
def hod_dashboard(request):
    return render(request, 'core/hod_dashboard.html')

@login_required
def staff_dashboard(request):
    return render(request, 'core/staff_dashboard.html')


# HOD logout view
@login_required
def hod_logout(request):
    logout(request)
    return redirect('hod_login')
# HOD manage staff add,delete,edi/update

@login_required
def manage_staff(request):
    staffs = CustomUser.objects.filter(role="STAFF")
    return render(request, "hod/manage_staff.html", {"staffs": staffs})


@login_required
def add_staff(request):
    if request.method == "POST":
        form = StaffForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            # 1) CustomUser banao
            user = CustomUser.objects.create_user(
                username=username,
                email=email,
                password=password,
                role="STAFF"
            )

            # 2) Staff banao
            Staff.objects.create(user=user)

            # 3)  Staff ko turant login karao
            login(request, user)

            # 4) ✅ Staff dashboard par redirect karo
            return redirect("staff_dashboard")

    else:
        form = StaffForm()

    return render(request, "hod/add_staff.html", {"form": form})


from django.shortcuts import get_object_or_404


@login_required
def update_staff(request, staff_id):
    staff = CustomUser.objects.get(id=staff_id, role="STAFF")
    if request.method == "POST":
        form = StaffForm(request.POST)
        if form.is_valid():
            staff.username = form.cleaned_data['username']
            staff.email = form.cleaned_data['email']
            staff.first_name = form.cleaned_data['first_name']
            staff.last_name = form.cleaned_data['last_name']
            if form.cleaned_data['password']:
                staff.set_password(form.cleaned_data['password'])
            staff.save()
            messages.success(request, "Staff updated successfully!")
            return redirect("manage_staff")
    else:
        form = StaffForm(initial={
            "username": staff.username,
            "email": staff.email,
            "first_name": staff.first_name,
            "last_name": staff.last_name,
        })
    return render(request, "hod/update_staff.html", {"form": form, "staff": staff})



@login_required
def delete_staff(request, staff_id):
    staff = CustomUser.objects.get(id=staff_id, role="STAFF")
    staff.delete()
    messages.success(request, "Staff deleted successfully!")
    return redirect("manage_staff")



# student  ko add , delete, edit krna

# ✅ Manage Student (list all students)
@login_required
def manage_student(request):
    students = Student.objects.all()
    return render(request, "hod/manage_student.html", {"students": students})

# ✅ Add Student
@login_required
def add_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            roll_no = form.cleaned_data['roll_no']

            # 1) Check if CustomUser already exists (deleted ya pehle ka user)
            user, created = CustomUser.objects.get_or_create(
                username=username,
                defaults={
                    "email": email,
                    "role": "STUDENT"
                }
            )

            # Agar naya user bana hai to password set karo
            if created:
                user.set_password(password)
            else:
                # Agar pehle se user exist karta hai to update kar do
                user.email = email
                user.role = "STUDENT"
                user.set_password(password)

            user.save()

            # 2) Student ko bhi check karo
            student, s_created = Student.objects.get_or_create(
                user=user,
                defaults={"roll_no": roll_no}
            )

            if not s_created:  # Agar pehle student exist tha
                student.roll_no = roll_no
                student.save()

            # 3) Login karao
            login(request, user)

            # 4) Dashboard redirect
            return redirect("student_dashboard")

    else:
        form = StudentForm()

    return render(request, "hod/add_student.html", {"form": form})

# def add_student(request):
#     if request.method == 'POST':
#         form = StudentForm(request.POST)
#         if form.is_valid():
#             # Create the User first
#             username = form.cleaned_data['username']
#             email = form.cleaned_data['email']
#             password = form.cleaned_data['password']
            
#             user = User.objects.create_user(username=username, email=email, password=password)
            
#             # Create the Student linked to the User
#             roll_no = form.cleaned_data['roll_no']
#             course = form.cleaned_data['course']
            
#             Student.objects.create(user=user, roll_no=roll_no, course=course)
            
#             messages.success(request, "Student added successfully!")
#             return redirect('manage_students')  # replace with your student list url

#     else:
#         form = StudentForm()

#     return render(request, 'hod/add_student.html', {'form': form})

# Update Student
# @login_required
# def update_student(request, student_id):
    # student = get_object_or_404(Student, id=student_id)
    # user = student.user

    # if request.method == 'POST':
    #     form = StudentForm(request.POST, instance=student)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('manage_students')
    # else:
    #     form = StudentForm(initial={
    #         'username': user.username,
    #         'email': user.email,
    #         'roll_no': student.roll_no,
    #         'course': student.course,
    #     })

    # return render(request, 'hod/update_student.html', context)
  
    # , {'form': form})
@login_required
def update_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            return redirect("manage_student")
    else:
        form = StudentForm(instance=student)
    return render(request, 'hod/update_student.html', {"form": form})


# ✅ Delete Student
@login_required
def delete_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    if student.user:
        student.user.delete()
    
    student.delete()
     # Reload the same page with updated students list
    students = Student.objects.all()

    # return render(request, 'hod/manage_students.html', {'students': students})
    messages.success(request, "Student deleted successfully!")
    return redirect('manage_students')

from .models import Course
from .forms import CourseForm

def manage_courses(request):
    courses = Course.objects.all()
    return render(request, 'hod/course_list.html', {'courses': courses})

# HOD Dashboard se course list
def course_list(request):
    courses = Course.objects.all()
    return render(request, 'hod/course_list.html', {'courses': courses})

# Add Course
def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manage_courses')
    else:
        form = CourseForm()
    return render(request, 'hod/add_course.html', {'form': form})
# Update Course
def update_course(request, course_id):
    course = Course.objects.get(id=course_id)
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            messages.success(request, "Course updated successfully!")
            return redirect('course_list')
    else:
        form = CourseForm(instance=course)
    return render(request, 'hod/add_course.html', {'form': form})

# Delete Course
def delete_course(request, course_id):
    course = Course.objects.get(id=course_id)
    course.delete()
    messages.success(request, "Course deleted successfully!")
    return redirect('course_list')



# hod/views.py

from .models import Attendance


# def add_attendance(request):
#     students = CustomUser.objects.filter(role='STUDENT')
#     staff_members = CustomUser.objects.filter(role='STAFF')
#     return render(request, 'hod/add_attendance.html'
#     , {
#         'students': students,
#         'staff_members': staff_members
#     })

from datetime import date

@login_required
def add_attendance(request):
    courses = Course.objects.all()
    students = CustomUser.objects.filter(role="STUDENT")

    if request.method == "POST":
        course_id = request.POST.get("course")
        course = Course.objects.get(id=course_id)
        staff = request.user  

        for student in students:
            status = request.POST.get(f"status_{student.id}")  # "Present"/"Absent"
            Attendance.objects.create(
                course=course,
                student=student,
                staff=staff,
                date=date.today(),
                status=status
            )

        messages.success(request, "Attendance marked successfully!")
        return redirect("view_attendance")

    return render(request, "hod/add_attendance.html", {
        "students": students,
        "courses": courses
    })
@login_required
def view_attendance(request):
    attendances = Attendance.objects.all().order_by('-date')
    return render(request, "hod/view_attendance.html", {"attendances": attendances})
