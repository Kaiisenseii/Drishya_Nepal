from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import DrishyaNepalUser
from django.contrib.auth import login
from service_provider.models import Photographer
# Create your views here.
def login_user(request):

    if request.user.is_authenticated:
        return redirect('index')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request=request, user=user)
            if "next" in request.GET:
                return redirect(request.GET['next'])
            return redirect("index")
        else:
            messages.error(request=request, message='Invalid Email or Password')     
    return render(request, 'login.html')

def logout_user(request):
    logout(request=request)
    return redirect('/')


def register_client(request):
    if request.method == "POST":
        print(request.POST, request.FILES)
        email = request.POST.get('email')
        username = request.POST.get('email')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone_number = request.POST.get('phone_number')
        profile_pic = request.FILES.get('profile_picture')
        address = request.POST.get('address')
        
        user = DrishyaNepalUser.objects.create(
            email=email,
            username=username,
            first_name=first_name,
            last_name=last_name,
            phone=phone_number,
            profile_pic=profile_pic,
            address=address
        )
        
        if user:
            user.set_password(password)
            user.save()
            login(request=request, user=user)
            messages.error(request=request, message='Registered Successfully.')
            return redirect('/')
        else:
            messages.error(request=request, message='Something Went Wrong')
            return redirect('register-client')
        
    return render(request, 'register-client.html')

def register_photographer(request):
    if request.method == "POST":
        print(request.POST, request.FILES)
        email = request.POST.get('email')
        username = request.POST.get('email')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone_number = request.POST.get('phone_number')
        profile_pic = request.FILES.get('profile_picture')
        experience = request.POST.get('experience')
        is_videographer = request.POST.get('is_videographer') == 'yes'
        address = request.POST.get('address')

        if is_videographer is None:
            is_videographer = False
            
        #check if email exists and assign it to photographer
        existing_user = DrishyaNepalUser.objects.filter(email=email)
        
        if existing_user.exists():
            existing_user= existing_user.first()
            existing_user.set_password(password)
            existing_user.is_customer = False
            existing_user.is_photographer = True
            existing_user.save()
            
            photographer = Photographer.objects.create(
                user=existing_user,
                experience= experience,
                is_videographer = is_videographer,
            )
            photographer.save()
            #hya neri photpgrapher ko detail lera mathi ko user jasari save garne
            login(request=request, user=existing_user)
            messages.error(request=request, message='Registered Successfully.')
            return redirect('index')
            
            
            
        
        user = DrishyaNepalUser.objects.create(
            email=email,
            username=username,
            first_name=first_name,
            last_name=last_name,
            phone=phone_number,
            profile_pic=profile_pic,
            is_photographer = True,
            address=address,
            is_customer=False
            
        )  
        if user:
            user.set_password(password)
            user.save()
            photographer = Photographer.objects.create(
                user=user,
                experience= experience,
                is_videographer = is_videographer,
            )
            photographer.save()
            #hya neri photpgrapher ko detail lera mathi ko user jasari save garne
            login(request=request, user=user)
            messages.error(request=request, message='Registered Successfully.')
            return redirect('index')
        else:
            messages.error(request=request, message='Something Went Wrong')
            return redirect('register-photographer')
        
    return render(request, 'register-photographer.html')


def password_forgot(request):
    return render(request, "forgot-pass.html")