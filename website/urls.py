from django.urls import path


from . import views

urlpatterns = [
    path('', views.home , name='index' ),
    path('about', views.about, name = 'about'),
    path('blog_details', views.blog_detail, name = 'blog_details'),
    path('blog', views.blog, name = 'blog'),
    path('elements', views.element, name = 'elements'),
    path('jobs', views.job, name = 'jobs'),
    path('contact', views.contact, name = 'contact'),
]
