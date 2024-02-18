from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordResetView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import (View)

from .forms import (LoginForm,
                    RegisterForm)


def register(request):
    """
    The register function is responsible for handling the registration of new users.
    It first checks if the user is already authenticated, and if so redirects them to the index page.
    If not, it then checks whether or not a POST request has been made (i.e., whether or not a form has been submitted).
    If so, it creates an instance of RegisterForm with that data and validates it; if valid, saves the form's data as a new User object in our database and redirects to login page; otherwise renders register template with invalid form instance passed as context. If no POST request was made (i.e.,
    
    :param request: Get the request object
    :return: The rendered register
    :doc-author: Trelent
    """
    if request.user.is_authenticated:
        return redirect(to="user_auth:signin")  # TODO

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to="user_auth:signin")  # TODO
        else:
            return render(request, "user_auth/register.html", context={"form": form})

    return render(request, "user_auth/register.html", context={"form": RegisterForm()})


def sign_in(request):
    """
    The sign_in function is a view that allows users to sign in.
        If the user is already signed in, they are redirected to the index page.
        If the request method is POST, then we authenticate and log them in if their username and password match.
        Otherwise, we redirect them back to login with an error message.
    
    :param request: Pass the request object to the view
    :return: A redirect to the index page if the user is already authenticated
    :doc-author: Trelent
    """
    if request.user.is_authenticated:
        return redirect(to="user_auth:signin")  # TODO
    if request.method == "POST":
        user = authenticate(
            username=request.POST["username"], password=request.POST["password"]
        )
        if user is None:
            messages.error(request, "Username or password didn't match")
            return redirect(to="user_auth:signin")  # TODO
        login(request, user)
        return redirect(to="user_auth:signin")  # TODO
    return render(request, "user_auth/login.html", context={"form": LoginForm()})


class EmailOnlyPasswordResetView(PasswordResetView):
    template_name = 'user_auth/password_reset.html'
    email_template_name = 'user_auth/password_reset_email.html'
    subject_template_name = 'user_auth/password_reset_subject.txt'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('user_auth:signin')  # TODO


@method_decorator(login_required, name="dispatch")
class SignOutView(View):
    def get(self, request):
        logout(request)
        return redirect(to="user_auth:index")  # TODO
