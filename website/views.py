from django.shortcuts import redirect, render
from django.contrib import messages
from service_provider.forms import EquipmentForm
from .models import Information, Developer, About
from service_provider.models import Photographer, Photo, Equipment, Services, Tag
from management.models import Hire
from management.forms import HireForm
from client.models import Customer, Feedback
from .forms import ServiceForm, ContactForm

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



def photographer_details_update(request, id):
    
    photographer= Photographer.objects.get(id=id)
    
    if "addtag" in request.GET:
        tag = Tag.objects.get(id=request.GET.get('addtag'))
        photographer.tags.add(tag)
        photographer.save()
        return redirect("photographer-update", photographer.id)
    
    if "deletetag" in request.GET:
        tag = Tag.objects.get(id=request.GET.get('deletetag'))
        photographer.tags.remove(tag)
        photographer.save()
        return redirect("photographer-update", photographer.id)
          
    
    if request.method == "POST":
        if "service_add_form" in request.POST:
            print(request.POST)
            form = ServiceForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("photographer-update", photographer.id)
    
        if "update_service" in request.POST:
            print(request.POST)
            photographer = Photographer.objects.get(id=request.POST.get('photographer'))
            service = Services.objects.get(id=request.POST.get('service'))
            name = request.POST['name']
            price = request.POST['price']
            description = request.POST['description']
            duration = request.POST['duration']
            
            service.name = name
            service.price = price
            service.description = description
            service.duration = duration
            service.save()
        
        if "equipment_add" in request.POST:
            print(request.POST, request.FILES)
            form = EquipmentForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect("photographer-update", photographer.id)
        
        if "update_equipment" in request.POST:
            print(request.POST, request.FILES)
            photographer = Photographer.objects.get(id=request.POST.get('photographer'))
            equipment = Equipment.objects.get(id=request.POST.FILES.get('equipment'))
            name = request.POST['name']
            description = request.POST['description']
            photo = request.POST.FILES['photo']
            
            equipment.name = name
            equipment.description = description
            equipment.photo = photo
            equipment.save()
            
        
        
        if "tags_add" in request.POST:
            photographer = Photographer.objects.get(id=id)
            name = request.POST.getlist('tags ')[0]
            tag= Tag.objects.get(name=name)
            photographer.tags.add(tag)
            photographer.save()
            return redirect("photographer-update", photographer.id)
            
            
    equipment_form = EquipmentForm()
    photographer = Photographer.objects.get(id=id)
    services = Services.objects.all().filter(photographer=photographer)
    equipments = Equipment.objects.all().filter(photographer=photographer)
    photos = Photo.objects.all().filter(photographer=photographer)
    tags = Tag.objects.all()
    context = {
        "photographer" : photographer, 
        "services" : services,
        'equipments' : equipments, 
        'photos' : photos,
        'equipment_form' : equipment_form,
        'tags' : tags,
    }
    
    return render(request, 'photographer-update.html', context)


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            messages.success(request=request, message='Thanks for contacting us. We will reach you soon.')
            form.save()
        return redirect("contact")
    return render(request, 'contact.html')
