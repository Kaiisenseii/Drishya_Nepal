from django.urls import path


from . import views

urlpatterns = [
    path('', views.home , name='index'),
    path('photographers', views.photographers, name="photographers"),
    path('rest_pg', views.rest_pg, name="rest-pg"),
    path('photographer/<int:id>', views.photographer_details, name="photographer-detail"),
    path('photographer-update/<int:id>', views.photographer_details_update, name = 'photographer-update'),
    path('about', views.about, name = "about"),
    path('contact', views.contact, name="contact"),
    path('dashboard', views.dashboard, name="dashboard"),
    path('dashboard-edit', views.dashboard_edit, name="dashboard-edit"),
    path('hires', views.hires, name="hires"),
    path('chat/<int:from_user>/<int:to_user>', views.chat, name="chat"),
    path('notification', views.notification, name="notification"),
]
