from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = "user_auth"

urlpatterns = [
    path("register/", views.register, name="register"),
    path("signin/", views.sign_in, name="signin"),
    path("signout/", views.SignOutView.as_view(), name="sign_out"),
    path('password_reset/', views.EmailOnlyPasswordResetView.as_view(), name='password_reset'),
    path('password-reset-confirm/<uidb64>/<token>/', views.CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='user_auth/password_reset_complete.html'), name='password_reset_complete'),
]
