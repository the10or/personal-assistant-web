from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse


from users.forms import LoginForm, ProfileForm, RegisterForm


def signupuser(request):
    if request.user.is_authenticated:
        return redirect(to="contacts:root")

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            if user.is_authenticated:
                logout(request)
                return redirect(reverse("contacts:root"))
            else:
                login(request, user)
                return redirect(reverse("contacts:root"))
        else:
            return render(request, "users/signup.html", context={"form": form})

    return render(request, "users/signup.html", context={"form": RegisterForm()})


def loginuser(request):
    if request.user.is_authenticated:
        return redirect("contacts:root")

    if request.method == "POST":
        user = authenticate(
            username=request.POST["username"], password=request.POST["password"]
        )
        if user is None:
            messages.error(request, "Username or password didn't match")
            return redirect(to="users:login")

        login(request, user)
        return redirect(to="contacts:root")

    return render(request, "users/login.html", context={"form": LoginForm()})


def logoutuser(request):
    if request.user.is_authenticated:
        logout(request)
        messages.info(request, "Logged out successfully!")
    return redirect("contacts:root")


@login_required
def profile(request):
    if request.method == "POST":
        profile_form = ProfileForm(
            request.POST, request.FILES, instance=request.user.profile
        )
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, "Your profile is updated successfully")
            return redirect(to="users:profile")

    profile_form = ProfileForm(instance=request.user.profile)
    return render(request, "users/profile.html", {"profile_form": profile_form})
