from django.urls import path


from . import views

urlpatterns = [
    path('', views.home , name='index' ),
    path('photographers', views.photographers, name="photographers"),
    path('photographer/<int:id>', views.photographer_details, name="photographer-detail"),
    path('about', views.about, name = "about"),
    path('login', views.login_user, name = "login"),
    path('register-client', views.register_client, name = "register-client"),
    path('register-photographer', views.register_photographer, name = "register-photographer"),
]
