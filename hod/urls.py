from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.hod_login, name='hod_login'),
    path('hod_dashboard/', views.hod_dashboard, name='hod_dashboard'),
    path('staff_dashboard/', views.staff_dashboard, name='staff_dashboard'),
    path('logout/', views.hod_logout, name='hod_logout'),
    # staff CRUD
    path('manage_staff/', views.manage_staff, name='manage_staff'),
    path('add_staff/', views.add_staff, name='add_staff'),
    path("update_staff/<int:staff_id>/", views.update_staff, name="update_staff"),
    path("delete_staff/<int:staff_id>/", views.delete_staff, name="delete_staff"),
    # Student CRUD
    path("manage_student/", views.manage_student, name="manage_student"),
    path("add_student/", views.add_student, name="add_student"),
    path("update_student/<int:student_id>/", views.update_student, name="update_student"),
    path("delete_student/<int:student_id>/", views.delete_student, name="delete_student"),

    path('manage_courses/', views.manage_courses, name='manage_courses'),
    path('courses/', views.course_list, name='course_list'),
    path('add_course/', views.add_course, name='add_course'),
    path('update_course/<int:course_id>/', views.update_course, name='update_course'),
    path('delete_course/<int:course_id>/', views.delete_course, name='delete_course'),


    path('add_attendance/', views.add_attendance, name='add_attendance'),
    path('view_attendance/', views.view_attendance, name='view_attendance'),



    
]
