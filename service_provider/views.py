from django.shortcuts import render, redirect, get_object_or_404
from .models import Services, Photographer, Equipment, Tag
# Create your views here.


def delete_service(request, id):
    service = Services.objects.get(id=id)
    photographer = Photographer.objects.get(id=service.photographer.id)
    service.delete()
    return redirect('photographer-update', photographer.id)

def delete_equipment(requet, id):
    equipment = Equipment.objects.get(id=id)
    photographer = Photographer.objects.get(id=equipment.photographer.id)
    equipment.delete()
    return redirect('photographer-update', photographer.id)

def tag_remove(request, id):
    photographer = get_object_or_404(Photographer, id=id)
    tag = get_object_or_404(Tag, id=request.POST.get('tag_id'))
    photographer.tags.remove(tag)
    photographer.save()
    return redirect('photographer_detail', id=photographer.id)
    
    