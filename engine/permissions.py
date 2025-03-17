import pdb
from functools import wraps
from django.http import HttpResponseForbidden

def manager_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.request.user.role == 'manager':
            return view_func(request, *args, **kwargs)
        return HttpResponseForbidden("Manager access required")
    return _wrapped_view

def user_or_manager_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.request.user.role in ['manager', 'user']:
            return view_func(request, *args, **kwargs)
        return HttpResponseForbidden("User or Manager access required")
    return _wrapped_view

def public_access(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.request.user.role in ['manager', 'user', 'public']:
            return view_func(request, *args, **kwargs)
        return HttpResponseForbidden("Access denied")
    return _wrapped_view
