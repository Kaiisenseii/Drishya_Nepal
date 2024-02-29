from django.shortcuts import render, redirect, get_object_or_404
from .models import Services, Photographer, Equipment, Tag, Photo
from django.contrib import messages
# Create your views here.


def delete_service(request, id):
    service = Services.objects.get(id=id)
    photographer = Photographer.objects.get(id=service.photographer.id)
    service.delete()
    messages.error(request=request, message="Service deleted successfully")
    return redirect('photographer-update', photographer.id)

def delete_equipment(request, id):
    equipment = Equipment.objects.get(id=id)
    photographer = Photographer.objects.get(id=equipment.photographer.id)
    equipment.delete()
    messages.error(request=request, message="Equipment Deleted Successfully.")
    return redirect('photographer-update', photographer.id)

def tag_remove(request, id):
    photographer = get_object_or_404(Photographer, id=id)
    tag = get_object_or_404(Tag, id=request.POST.get('tag_id'))
    photographer.tags.remove(tag)
    photographer.save()
    messages.error(request=request, message="Tag removed")
    return redirect('photographer_detail', id=photographer.id)

def photo_remove(request, id):
    photo = Photo.objects.get(id=id)
    photographer = Photographer.objects.get(id=photo.photographer.id)
    photo.delete()
    messages.error(request=request, message="Photo Removed")
    return redirect('photographer-update', photographer.id) 
    
    