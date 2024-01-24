from django.urls import path
from . import views


urlpatterns = [
    path('delete-service/<int:id>', views.delete_service, name="delete-service" ),
    path('delete-equipment/<int:id>', views.delete_equipment, name = "delete-equipment"),
    path('tag_remove/<int:id>', views.tag_remove, name='tag_remove')
]
