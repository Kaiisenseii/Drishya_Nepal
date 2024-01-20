from django.urls import path


from . import views

urlpatterns = [
    path('', views.home , name='index' ),
    path('photographers', views.photgraphers, name="photographers"),
    path('photographer/<int:id>', views.photographer_details, name="photographer-detail"),
    path('about', views.about, name="about"),
]
