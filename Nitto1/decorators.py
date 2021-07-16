from django.http import HttpResponse
from django.shortcuts import redirect


#If A User Is Logged In Or Not
def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('adminProf')
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func    


#Loggin Depending on django groups
def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):

            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('You Are Not Authorized')    
        return wrapper_func
    return decorator    

#admin only
def admin_only(view_func):
    def wrapper_func(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
        if group == 'customer':
            return redirect('adminProf')    
        if group == 'admin':
            return view_func(request, *args, **kwargs)
    return wrapper_func