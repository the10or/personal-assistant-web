from django.shortcuts import redirect

def user_not_authenticated(function=None, redirect_url='user_auth:signin'):
    """
    Decorator for views that checks that the user is NOT logged in, redirecting
    to the signin page.
    """
    def decorator(view_func):
        def _wrapped_view(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return redirect(redirect_url)
                
            return view_func(request, *args, **kwargs)

        return _wrapped_view

    if function:
        return decorator(function)

    return decorator
