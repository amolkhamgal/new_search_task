from django.shortcuts import redirect

def login_or_register_required(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('register')
        return view_func(request, *args, **kwargs)
    return wrapper
