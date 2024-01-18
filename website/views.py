from django.shortcuts import render
from .models import Website, Developer
from service_provider.models import Photographer, Photo, Equipment, Services
from management.models import Hire
from client.models import Customer, Feedback

# Create your views here.

def home(request):
    websites = Website.objects.all()
    developers = Developer.objects.all()
    photographers = Photographer.objects.all()
    photos = Photo.objects.all()
    equipments = Equipment.objects.all()
    services = Services.objects.all()
    hires = Hire.objects.all()
    customers = Customer.objects.all()
    feedback = Feedback.objects.all()

    context = {
        'websites' : websites,
        'developers' : developers,
        'photographers' : photographers,
        'photos' : photos,
        'equipments' : equipments,
        'services' : services,
        'hires' : hires,
        'customers': customers,
        'feedback' : feedback
    }
    return render(request, 'index.html' , context)

def about(request):

    websites = Website.objects.all()
    developers = Developer.objects.all()
    photographers = Photographer.objects.all()
    photos = Photo.objects.all()
    equipments = Equipment.objects.all()
    services = Services.objects.all()
    hires = Hire.objects.all()
    customers = Customer.objects.all()
    feedback = Feedback.objects.all()
    

    context = {
        'websites' : websites,
        'developers' : developers,
        'photographers' : photographers,
        'photos' : photos,
        'equipments' : equipments,
        'services' : services,
        'hires' : hires,
        'customers': customers,
        'feedback' : feedback
    }
    return render(request, 'about.html', context)

def blog_detail(request):
    websites = Website.objects.all()
    developers = Developer.objects.all()
    photographers = Photographer.objects.all()
    photos = Photo.objects.all()
    equipments = Equipment.objects.all()
    services = Services.objects.all()
    hires = Hire.objects.all()
    customers = Customer.objects.all()
    feedback = Feedback.objects.all()

    context = {
        'websites' : websites,
        'developers' : developers,
        'photographers' : photographers,
        'photos' : photos,
        'equipments' : equipments,
        'services' : services,
        'hires' : hires,
        'customers': customers,
        'feedback' : feedback
    }
    return render(request, "blog_details.html", context)

def blog(request):
    websites = Website.objects.all()
    developers = Developer.objects.all()
    photographers = Photographer.objects.all()
    photos = Photo.objects.all()
    equipments = Equipment.objects.all()
    services = Services.objects.all()
    hires = Hire.objects.all()
    customers = Customer.objects.all()
    feedback = Feedback.objects.all()

    context = {
        'websites' : websites,
        'developers' : developers,
        'photographers' : photographers,
        'photos' : photos,
        'equipments' : equipments,
        'services' : services,
        'hires' : hires,
        'customers': customers,
        'feedback' : feedback
    }
    return render(request, "blog.html", context)

def element(request):
    websites = Website.objects.all()
    developers = Developer.objects.all()
    photographers = Photographer.objects.all()
    photos = Photo.objects.all()
    equipments = Equipment.objects.all()
    services = Services.objects.all()
    hires = Hire.objects.all()
    customers = Customer.objects.all()
    feedback = Feedback.objects.all()

    context = {
        'websites' : websites,
        'developers' : developers,
        'photographers' : photographers,
        'photos' : photos,
        'equipments' : equipments,
        'services' : services,
        'hires' : hires,
        'customers': customers,
        'feedback' : feedback
    }
    return render(request, "elements.html", context)

def job(request):
    websites = Website.objects.all()
    developers = Developer.objects.all()
    photographers = Photographer.objects.all()
    photos = Photo.objects.all()
    equipments = Equipment.objects.all()
    services = Services.objects.all()
    hires = Hire.objects.all()
    customers = Customer.objects.all()
    feedback = Feedback.objects.all()

    context = {
        'websites' : websites,
        'developers' : developers,
        'photographers' : photographers,
        'photos' : photos,
        'equipments' : equipments,
        'services' : services,
        'hires' : hires,
        'customers': customers,
        'feedback' : feedback
    }
    return render(request, 'jobs.html', context)

def contact(request):
    websites = Website.objects.all()
    developers = Developer.objects.all()
    photographers = Photographer.objects.all()
    photos = Photo.objects.all()
    equipments = Equipment.objects.all()
    services = Services.objects.all()
    hires = Hire.objects.all()
    customers = Customer.objects.all()
    feedback = Feedback.objects.all()

    context = {
        'websites' : websites,
        'developers' : developers,
        'photographers' : photographers,
        'photos' : photos,
        'equipments' : equipments,
        'services' : services,
        'hires' : hires,
        'customers': customers,
        'feedback' : feedback
    }
    return render(request, "contact.html", context)