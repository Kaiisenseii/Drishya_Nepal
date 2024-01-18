from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def blog_detail(request):
    return render(request, "blog_details.html")

def blog(request):
    return render(request, "blog.html")

def element(request):
    return render(request, "elements.html")

def job(request):
    return render(request, 'jobs.html')

def contact(request):
    return render(request, "contact.html")