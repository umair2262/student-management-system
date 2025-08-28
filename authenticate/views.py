from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse_lazy
from .forms import RegisterForm, ProfileUpdateForm
from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)


# Register View

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}. You can now login.')
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'authenticate/register.html', {'form': form})

# -----------------------------
# Login View
# -----------------------------
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.role == 'HOD':
                return redirect('hod_dashboard')
            elif user.role == 'STAFF':
                return redirect('staff_dashboard')
            else:
                return redirect('student_dashboard')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'authenticate/login.html')


# Logout View

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')


# Profile View

@login_required
def profile_view(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully!")
            return redirect('profile')
    else:
        form = ProfileUpdateForm(instance=request.user)
    return render(request, 'authenticate/profile.html', {'form': form})


# Password Reset Views

class CustomPasswordResetView(PasswordResetView):
    template_name = 'authenticate/password_reset.html'
    email_template_name = 'authenticate/password_reset_email.html'
    subject_template_name = 'authenticate/password_reset_subject.txt'
    success_url = reverse_lazy('password_reset_done')

class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'authenticate/password_reset_done.html'

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'authenticate/password_reset_confirm.html'
    success_url = reverse_lazy('password_reset_complete')

class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'authenticate/password_reset_complete.html'


# Dashboard views
@login_required
def hod_dashboard(request):
    return render(request, 'core/hod_dashboard.html')

@login_required
def staff_dashboard(request):
    return render(request, 'core/staff_dashboard.html')

@login_required
def student_dashboard(request):
    return render(request, 'core/student_dashboard.html')



