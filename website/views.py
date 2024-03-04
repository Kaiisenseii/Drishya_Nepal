from django.shortcuts import redirect, render
from django.contrib import messages
from service_provider.forms import EquipmentForm
from .models import Information, Developer, About
from service_provider.models import Photographer, Photo, Equipment, Services, Tag
from management.models import Hire, Testimonial
from management.forms import HireForm
from client.models import Customer, Feedback
from .forms import ServiceForm, ContactForm, PhotographerPhotoForm
from Authentication.models import Chat, DrishyaNepalUser, Notification
from django.contrib.auth.decorators import login_required
from Authentication.forms import ChatForm
from django.db.models import Q
# Create your views here.
from client.forms import FeedBackForm
from django.http.response import JsonResponse
from django.db.models import Avg, Count
from Authentication.views import send_notification


def recommend_photographers():
    # Annotate each photographer with their average rating and count of feedbacks
    photographers = Photographer.objects.annotate(
        avg_rating=Avg('feedback__rating'),
        feedback_count=Count('feedback', distinct=True),
        photo_count=Count('photo', distinct=True),
        service_count=Count('services', distinct=True)
    )

    # Normalize scores (optional, for balanced weighting across different scales)
    max_rating = photographers.aggregate(max_rating=Avg('avg_rating'))['max_rating'] or 1
    max_feedback_count = photographers.aggregate(max_feedback_count=Count('feedback'))['max_feedback_count'] or 1
    max_photo_count = photographers.aggregate(max_photo_count=Count('photo'))['max_photo_count'] or 1
    max_service_count = photographers.aggregate(max_service_count=Count('services'))['max_service_count'] or 1

    # Compute a combined score for each photographer
    scored_photographers = []
    for photographer in photographers:
        score = (
            (photographer.avg_rating / max_rating) * 0.4 +  # Weighting average rating as 40% of the score
            (photographer.feedback_count / max_feedback_count) * 0.2 +  # Weighting feedback count as 20% of the score
            (photographer.photo_count / max_photo_count) * 0.2 +  # Weighting photo count as 20% of the score
            (photographer.service_count / max_service_count) * 0.2  # Weighting service count as 20% of the score
        )
        scored_photographers.append((photographer, score))

    # Sort photographers by their computed score in descending order
    top_photographers = sorted(scored_photographers, key=lambda x: x[1], reverse=True)

    # Return the top N photographers based on the computed scores
    return [photographer for photographer, _ in top_photographers][:5]  


def home(request):
    info = Information.objects.first()
    photographers = Photographer.objects.all()[:3]
    photos = Photo.objects.all()
    abouts = About.objects.all()
    testimonials = Testimonial.objects.all()
    # unique set of photographer.user.address
    addresses = set([p.user.address for p in photographers])
    
    
    
    context = {
        'info' : info,
        'photographers' : photographers,
        'photos' : photos,
        'abouts' : abouts,
        'testimonials' :  testimonials,
        'addresses' : addresses,
        'recommended_photographers':  recommend_photographers(),

    }
    return render(request, 'index.html' , context)

def rest_pg(request):
    photographers = Photographer.objects.all().values()
    return JsonResponse({'photographers' : list(photographers)})
    


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
        form = HireForm(request.POST)
        if form.is_valid():
            hire = form.save()
            #send notififcation
            photographer = hire.photographer
            send_notification(user=photographer, message="You are hired by. {0}. Please view your hires page".format(hire.customer))
            return redirect('hires')
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
            
            
    services = Services.objects.all().filter(photographer=photographer)
    equipments = Equipment.objects.all().filter(photographer=photographer)
    photos = Photo.objects.all().filter(photographer=photographer)
    reviews = Feedback.objects.all().filter(photographer=photographer)
    context = {
        "photographer" : photographer, 
        "services" : services,
        'equipments' : equipments, 
        'photos' : photos,
        'is_owner': is_owner,
        'reviews' : reviews,
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
    status_choices = Photographer.STATUS_CHOICES
    
    
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
        messages.success(request=request, message='Tags added successfully!')
        return redirect("photographer-update", photographer.id)
    
    if "deletetag" in request.GET:
        tag = Tag.objects.get(id=request.GET.get('deletetag'))
        photographer.tags.remove(tag)
        photographer.save()
        messages.success(request=request, message='Service Deleted successfully!')
        return redirect("photographer-update", photographer.id)

    
    if request.method == "POST":
        if "service_add_form" in request.POST:
            print(request.POST)
            form = ServiceForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request=request, message='Service added successfully!')
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
            messages.success(request=request, message='Service updated successfully!')
            return redirect("photographer-update", photographer.id)
        
        if "equipment_add" in request.POST:
            print(request.POST, request.FILES)
            form = EquipmentForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request=request, message='Equipment Added successfully')
                return redirect("photographer-update", photographer.id)
            else:
                print(form.errors)
        
        if "update_equipment" in request.POST:
            print(request.POST, request.FILES)
            photographer = Photographer.objects.get(id=request.POST.get('photographer'))
            equipment = Equipment.objects.get(id=request.POST.get('equipment'))
            name = request.POST['name']
            description = request.POST['description']
            photo = request.FILES['photo']
            
            equipment.name = name
            equipment.description = description
            equipment.photo = photo
            equipment.save()
            messages.success(request=request, message='Equipment updated successfully!')
            return redirect("photographer-update", photographer.id)
            
        if "update_profile_pic" in request.POST:
            print(request.FILES)
            photographer = Photographer.objects.get(id=request.POST.get('photographer'))
            profile_pic = request.FILES['profile_pic']
            photographer.user.profile_pic = profile_pic
            photographer.save()
            messages.success(request=request, message='Profile Picture updated successfully!')
            return redirect("photographer-update", photographer.id)
            
            
        
        if "tags_add" in request.POST:
            photographer = Photographer.objects.get(id=id)
            name = request.POST.getlist('tags ')[0]
            tag= Tag.objects.get(name=name)
            photographer.tags.add(tag)
            photographer.save()
            messages.success(request=request, message='Tags added successfully!')
            return redirect("photographer-update", photographer.id)
        
        if "photographer_photo_add" in request.POST:
            print(request.POST, request.FILES)
            form = PhotographerPhotoForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request=request, message='Photo added successfully!')
                return redirect("photographer-update", photographer.id)
            else:
                messages.success(request=request, message='Photo doesnot added')
                print(form.errors)
        
        if "status" in request.POST:  # change status of the user
            status = request.POST['status']
            
            if status == '':
                status = photographer.status
            photographer.status = status
            photographer.save()
            messages.success(request=request, message='Status updated successfully!')
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
        'status_choices' : status_choices,
        
    }
    
    return render(request, 'photographer-update.html', context)


def contact(request):
    developers = Developer.objects.all()
    context = {
        'developers' : developers,
    }
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request=request, message='Thanks for contacting us. We will reach you soon.')
        else:
            messages.error(request=request,message=('Contact Failed. Please Check Your Credentials Below or Wrong Message is typed!!'))
        return redirect("contact")
    return render(request, 'contact.html', context)

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
            messages.success(request=request, message='Profile Picture Updated Successfully')
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
                messages.success(request=request, message='Details Updated Successfully')
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
                messages.success(request=request, message='Details Updated Successfully')
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
    if request.method == "POST":
        if "rate" in request.POST:
            feedback = FeedBackForm(request.POST)
            if feedback.is_valid():
                feedback.save()
                messages.success(request=request,  message="Feedback Sent Successfully")
                return redirect('hires')
            else:
                messages.error(request=request,  message="Feedback Sent Unsuccessful")
                print(feedback.errors)
    
    if request.user.is_customer:
        hires = Hire.objects.all().filter(customer=request.user)
    if request.user.is_photographer:
        print(request.user)
        hires = Hire.objects.all().filter(photographer=request.user)
    
  
    context = {
        'hires': hires
    }
    return render(request, 'hires.html', context)

def notification(request):

    return render(request, "notification.html", {'notifications': Notification.objects.filter(user=request.user)})


