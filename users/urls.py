from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from users.views import register_view, profile_view


urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name="users/login.html"),name="users-login"),
    path('logout/', auth_views.LogoutView.as_view(template_name="users/logout.html"),name="users-logout"),
    path('password-reset/',
        auth_views.PasswordResetView.as_view(template_name="users/password_reset.html"),
        name="users-password-reset"),
    path('password-reset/done',
        auth_views.PasswordResetDoneView.as_view(template_name="users/password_reset_done.html"),
        name="password_reset_done"),
    path('password-reset-confirm/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(template_name="users/password_reset_confirm.html"),
        name="password_reset_confirm"),
    path('register/',register_view, name="users-register"),
    path('profile/',profile_view, name="users-profile"),
]