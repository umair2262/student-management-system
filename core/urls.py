from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Main homepage
    path('base/', views.home_view, name='base'),  # Base template test view

    # Dashboards
    path('hod_dashboard/', views.hod_dashboard, name='hod_dashboard'),
    path('staff_dashboard/', views.staff_dashboard, name='staff_dashboard'),
    path('student_dashboard/', views.student_dashboard, name='student_dashboard'),
    
]
