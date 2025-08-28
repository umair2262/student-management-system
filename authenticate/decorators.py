from django.http import HttpResponse
from django.shortcuts import redirect

def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            if request.user.is_authenticated:
                if request.user.role in allowed_roles:
                    return view_func(request, *args, **kwargs)
                else:
                    return HttpResponse('Unauthorized: You cannot access this page.')
            else:
                return redirect('login')
        return wrapper_func
    return decorator
