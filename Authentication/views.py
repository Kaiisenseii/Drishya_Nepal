from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def login_user(request):
    
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request=request, user=user)
            return redirect("index")       
    return render(request, 'login.html')

def logout_user(request):
    logout(request=request)
    return redirect('/')


def register_client(request):
    
    return render(request, 'register-client.html')

def register_photographer(request):
    return render(request, 'register-photographer.html')