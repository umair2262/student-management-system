from django.urls import path
from . import views

urlpatterns =[
    path('student_dashboard/', views.student_dashboard, name='student_dashboard'),
    path('view_attendance/', views.view_attendance, name='view_attendance'),
    path("courses/", views.view_courses, name="view_courses"),
]