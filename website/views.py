from django.shortcuts import render
from .models import Information, Developer
from service_provider.models import Photographer, Photo, Equipment, Services
from management.models import Hire
from client.models import Customer, Feedback

# Create your views here.

def home(request):
    info = Information.objects.first()
    developers = Developer.objects.all()
    photographers = Photographer.objects.all()
    photos = Photo.objects.all()

    context = {
        'info' : info,
        'developers' : developers,
        'photographers' : photographers,
        'photos' : photos,
       
    }
    return render(request, 'index.html' , context)



def photgraphers(request):
    photographers = Photographer.objects.all()
    photos = Photo.objects.all()

    context = {
        'photographers' : photographers,
        'photos' : photos,
       
    }
    return render(request, 'photographers.html' , context)


def photographer_details(request, id):
    photographer = Photographer.objects.get(id=id)
    services = Services.objects.all().filter(photographer=photographer)
    equipments = Equipment.objects.all().filter(photographer=photographer)
    context = {
        "photographer" : photographer, 
        "services" : services,
        'equipments' : equipments, 
    }
    
    return render(request, 'photographer-details.html', context)

def about(request):
    return render(request, 'about.html')