from django.urls import path
from . import views


urlpatterns = [
    path('delete-service/<int:id>', views.delete_service, name="delete-service" ),
]
