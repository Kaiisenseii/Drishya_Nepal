from django.shortcuts import render
from .models import Information, Developer, About
from service_provider.models import Photographer, Photo, Equipment, Services
from management.models import Hire
from management.forms import HireForm
from client.models import Customer, Feedback

# Create your views here.

def home(request):
    info = Information.objects.first()
    developers = Developer.objects.all()
    photographers = Photographer.objects.all()
    photos = Photo.objects.all()
    abouts = About.objects.all()

    context = {
        'info' : info,
        'developers' : developers,
        'photographers' : photographers,
        'photos' : photos,
        'abouts' : abouts,
       
    }
    return render(request, 'index.html' , context)



def photographers(request):
    photographers = Photographer.objects.all()
    photos = Photo.objects.all()

    context = {
        'photographers' : photographers,
        'photos' : photos,
       
    }
    return render(request, 'photographers.html' , context)


def photographer_details(request, id):
    
    #for hire photgrapher
    if request.method == "POST" and "hire_form" in request.POST :
        print(request.POST)
        form = HireForm(request.POST)
        if form.is_valid():
            form.save()
            #send messages for success
        else:
            #send message to fornt end with errors
            print(form.errors)
        
    
    photographer = Photographer.objects.get(id=id)
    services = Services.objects.all().filter(photographer=photographer)
    equipments = Equipment.objects.all().filter(photographer=photographer)
    photos = Photo.objects.all().filter(photographer=photographer)
    context = {
        "photographer" : photographer, 
        "services" : services,
        'equipments' : equipments, 
        'photos' : photos,
    }
    
    return render(request, 'photographer-details.html', context)

def about(request):
    abouts = About.objects.all()
    context = {
        "abouts" : abouts,
    }
    return render(request, 'about.html', context)

def login_user(request):
    return render(request, 'login.html')

def register_client(request):
    return render(request, 'register-client.html')

def register_photographer(request):
    return render(request, 'register-photographer.html')