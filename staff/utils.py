# staff/utils.py
from core.models import Student
from authenticate.models import CustomUser
from hod.models import Course

def get_students_for_staff(staff_user):
    # staff ke courses le lo
    courses = Course.objects.filter(staff=staff_user)
    # un courses ke students le lo
    students = CustomUser.objects.filter(
        role='STUDENT',
        courses_students__in=courses
    ).distinct()
    return students

# def get_students_for_staff(staff_user):
    # Ye function staff ke students return karega
    # return Student.objects.all()
