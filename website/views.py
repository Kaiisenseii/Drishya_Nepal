from django.shortcuts import redirect, render
from django.contrib import messages
from service_provider.forms import EquipmentForm
from .models import Information, Developer, About
from service_provider.models import Photographer, Photo, Equipment, Services, Tag
from management.models import Hire, Testimonial
from management.forms import HireForm
from client.models import Customer, Feedback
from .forms import ServiceForm, ContactForm
from Authentication.models import Chat, DrishyaNepalUser
from django.contrib.auth.decorators import login_required
from Authentication.forms import ChatForm
from django.db.models import Q
# Create your views here.

def home(request):
    info = Information.objects.first()
    developers = Developer.objects.all()
    photographers = Photographer.objects.all()
    photos = Photo.objects.all()
    abouts = About.objects.all()
    testimonials = Testimonial.objects.all()

    context = {
        'info' : info,
        'developers' : developers,
        'photographers' : photographers,
        'photos' : photos,
        'abouts' : abouts,
        'testimonials' :  testimonials,
       
    }
    return render(request, 'index.html' , context)



def photographers(request):
    search_text = ""
    location = ""
    photographers = Photographer.objects.all()
    photos = Photo.objects.all()
    
    # unique set of photographer.user.address
    addresses = set([p.user.address for p in photographers])
    
    if request.GET.get('search'):
        search_text = request.GET.get('search')
        photographers = Photographer.objects.filter(Q(user__first_name__icontains=search_text) | Q(user__address__icontains=search_text))
        
    if request.GET.get('select'):
        location = request.GET.get('select')
        photographers = [p for p in photographers if p.user.address == location]
        

    context = {
        'photographers' : photographers,
        'photos' : photos,
        'search_text' : search_text,
        'addresses' : addresses,
        'location' : location,
       
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
            
    is_owner = False
    photographer = Photographer.objects.get(id=id)
    
    if request.user.is_authenticated:
        user = DrishyaNepalUser.objects.get(id=request.user.id)
        if int(user.id) == int(photographer.user.id):
            is_owner = True 
        else:
            is_owner = False
            
            
    print(is_owner)  
    services = Services.objects.all().filter(photographer=photographer)
    equipments = Equipment.objects.all().filter(photographer=photographer)
    photos = Photo.objects.all().filter(photographer=photographer)
    context = {
        "photographer" : photographer, 
        "services" : services,
        'equipments' : equipments, 
        'photos' : photos,
        'is_owner': is_owner
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
    
    if request.user.is_authenticated:
        user = DrishyaNepalUser.objects.get(id=request.user.id)
        if int(user.id) == int(photographer.user.id):
            is_owner = True 
        else:
            is_owner = False
            return redirect('/')
    
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
            return redirect("photographer-update", photographer.id)
        
        if "equipment_add" in request.POST:
            print(request.POST, request.FILES)
            form = EquipmentForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect("photographer-update", photographer.id)
            else:
                print(form.errors)
        
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
            return redirect("photographer-update", photographer.id)
            
        if "update_profile_pic" in request.POST:
            print(request.FILES)
            photographer = Photographer.objects.get(id=request.POST.get('photographer'))
            profile_pic = request.FILES['profile_pic']
            photographer.user.profile_pic = profile_pic
            photographer.save()
            return redirect("photographer-update", photographer.id)
            
            
        
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

def dashboard(request):
    user = DrishyaNepalUser.objects.get(id=request.user.id)
    
    print(user)
    context={
        'user' : user,
    }
    return render (request, "dashboard.html", context)

@login_required
def dashboard_edit(request):
    user = DrishyaNepalUser.objects.get(id=request.user.id)
    if request.method == "POST":
        if "update_profile" in request.POST:
            profile_pic = request.FILES['profile_pic_edit']
            user.profile_pic = profile_pic
            user.save()
            return redirect("dashboard")
           
    if user.is_photographer:
        photographer = Photographer.objects.get(id=user.photographer.id)
        if request.method == "POST":
            print(request.POST) 
            if "details_update"  in request.POST:
                print(request.POST)
                user.first_name = request.POST['f_name']
                user.last_name = request.POST['l_name']
                user.phone = request.POST['p_number']
                user.address = request.POST['location']
                user.email = request.POST['e_mail']
                photographer.experience = request.POST['e_xperience']
                user.save()
                photographer.save()
                return redirect("dashboard")
    else:
        if request.method == "POST":
            if "details_update"  in request.POST:
                user.first_name = request.POST['f_name']
                user.last_name = request.POST['l_name']
                user.phone = request.POST['p_number']
                user.address = request.POST['location']
                user.email = request.POST['e_mail']
                user.save()
                return redirect("dashboard")
    return render (request, "dashboard-edit.html")


def chat(request, from_user, to_user):
    to_user_data = DrishyaNepalUser.objects.get(id=to_user)
    from_user_data = DrishyaNepalUser.objects.get(id=from_user)
    
    if request.method == "POST":
        form = ChatForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('chat',  from_user=from_user, to_user=to_user)
        else:
            print(form.errors)
    
    chats = Chat.objects.filter(
        Q(from_user=from_user_data, to_user=to_user_data) | Q(from_user=to_user_data, to_user=from_user_data)
    ).order_by('created_at')  # You may want to order the messages by creation time.

    # Separate messages into 'to' and 'from' lists
    to_user_chats = chats.filter(to_user=from_user_data)
    from_user_chats = chats.filter(from_user=from_user_data)

    context = {
        'to_user': to_user_data,
        'from_user': from_user_data,
        'to_user_chats': to_user_chats,
        'from_user_chats': from_user_chats,
        'chats': chats,
    }

    return render(request, "chat.html", context)

def hires(request):
    print(request.user.is_photographer)
    if request.user.is_customer:
        hires = Hire.objects.all().filter(customer=request.user)
        print(hires)
    if request.user.is_photographer:
        print(request.user)
        hires = Hire.objects.all().filter(photographer=request.user)
        # print(hires)
    context = {
        'hires': hires
    }
    return render(request, 'hires.html', context)

def views_stars(request):
    pass