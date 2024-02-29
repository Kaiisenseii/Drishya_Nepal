from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import DrishyaNepalUser, Otp
from django.contrib.auth import login
from service_provider.models import Photographer
import random
import smtplib
from email.mime.text import MIMEText

def send_email(subject, body, recipient):
    sender = "drishyanepal.2024@gmail.com"
    password = "ywkr ztme kygh wrvo"
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recipient  
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
        smtp_server.login(sender, password)
        smtp_server.sendmail(sender, recipient, msg.as_string())
    print("Message sent!")




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
            messages.success(request=request, message="Login Successful. Welcome to Drishya Nepal")
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
            otp = random.randint(100000,999999)
            otp_obj = Otp.objects.create(user=user, otp=otp)
            otp_obj.save()
            send_email("Drishya Nepal Welcome.", f"Your otp is : {otp} ", user.email)
            messages.success(request=request, message="OTP has been sent to your registered Email")
            return redirect("register-otp") 
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
            otp = random.randint(100000,999999)
            otp_obj = Otp.objects.create(user=user, otp=otp)
            otp_obj.save()
            send_email("Drishya Nepal Welcome.", f"Your otp is : {otp} ", user.email)
            messages.success(request=request, message="OTP has been sent to your registered Email")
            return redirect("register-otp")  
        else:
            messages.error(request=request, message='Something Went Wrong')
            return redirect('register-photographer')
        
    return render(request, 'register-photographer.html')


def password_confirm(request, user_id):
    user = DrishyaNepalUser.objects.get(id=user_id)
    if request.method == 'POST':
            new_password = request.POST['new_password']
            confirm_password = request.POST['confirm_password']

            if new_password == confirm_password:
                user = request.user
                user.set_password(new_password)
                user.save()
                return redirect('login')
            else:
                messages.error(request=request, message='Passwords do not match')
                return render(request, 'password_confirm.html')
    else:
            return render(request, "password-confirm.html")

def password_reset(request):
    if request.method == "POST":
        email = request.POST.get("email")
        user = DrishyaNepalUser.objects.filter(email=email)
        if not user.exists():
            messages.error(request=request, message="Email not found")
            return redirect("pass-reset")
        else:
            user = user.first()
            #generate otp from random of length 6
            otp = random.randint(100000,999999)
            otp_obj = Otp.objects.create(user=user, otp=otp)
            otp_obj.save()
            send_email("Drishya Nepal Passowrd Reset.", f"Your otp is : {otp} ", user.email)
            messages.success(request=request, message="OTP has been sent to your registered Email")
            return redirect("otp")            
    return render(request, "pass-reset.html")

def otp(request):
    if request.method == "POST":
        otp = request.POST.get("otp")
        otp_obj = Otp.objects.filter(otp=otp).order_by('created_at')
        if not otp_obj.exists():
            messages.error(request=request, message="OTP don't match.")
            return redirect("otp")
        else:
            user = otp_obj.first().user
            messages.success(request=request, message="OTP matched. Please Reset your password.")
            return redirect('password-confirm', user.id)
    return render(request, "otp.html")

def register_otp(request):
    if request.method == "POST":
        otp = request.POST.get("otp")
        otp_obj = Otp.objects.filter(otp=otp).order_by('created_at')
        if not otp_obj.exists():
            messages.error(request=request, message="OTP don't match.")
            return redirect("register-otp")
        else:
            user = otp_obj.first().user
            login(request=request, user=user)
            messages.success(request=request, message="Welcome to Drishya Nepal.")
            return redirect('/')
    return render(request, "register-otp.html")