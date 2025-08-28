# staff/utils.py
from core.models import Student

def get_students_for_staff(staff_user):
    # Ye function staff ke students return karega
    return Student.objects.all()
