from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login_user, name = "login"),
    path('logout', views.logout_user, name = "logout"),
    path('register-client', views.register_client, name = "register-client"),
    path('register-photographer', views.register_photographer, name = "register-photographer"),
    path('password-confirm/<int:user_id>', views.password_confirm, name='password-confirm'),
    path('pass-reset', views.password_reset, name='pass-reset'),
    path('otp', views.otp, name='otp'),
    path('register-otp', views.register_otp, name='register-otp'),
]
