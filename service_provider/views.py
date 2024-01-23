from django.shortcuts import render, redirect
from .models import Services, Photographer
# Create your views here.


def delete_service(request, id):
    service = Services.objects.get(id=id)
    photographer = Photographer.objects.get(id=service.photographer.id)
    service.delete()
    return redirect('photographer-update', photographer.id)
    