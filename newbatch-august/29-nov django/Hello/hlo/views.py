from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("This is home page")

def homepage(request):
    return render(request, "home.html")