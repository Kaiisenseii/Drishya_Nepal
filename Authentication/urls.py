from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login_user, name = "login"),
    path('logout', views.logout_user, name = "logout"),
    path('register-client', views.register_client, name = "register-client"),
    path('register-photographer', views.register_photographer, name = "register-photographer"),
]
