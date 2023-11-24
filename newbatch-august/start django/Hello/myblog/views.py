from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def hlo(request):
    return HttpResponse("this is my first url hit")

def home(request):
    return HttpResponse("this is my home page")

def contact(request):
    return HttpResponse("this is my contact us page")

def about(request):
    return HttpResponse("this is my about us page")