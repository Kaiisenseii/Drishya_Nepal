from django.urls import path
from . import views

urlpatterns = [
    path('', views.home , name='index'),
    path('photographers', views.photographers, name="photographers"),
    path('photographer/<int:id>', views.photographer_details, name="photographer-detail"),
    path('photographer-update/<int:id>', views.photographer_details_update, name = 'photographer-update'),
    path('about', views.about, name = "about"),
    path('contact', views.contact, name="contact")
    
]
