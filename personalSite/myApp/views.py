from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return render(request, "myApp/base.html")

def projects(request):
    return render(request, "myApp/projects.html")

def education(request):
    return render(request, "myApp/education.html")

def work(request):
    return render(request, "myApp/work.html")