from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return HttpResponse("this is home page")


def aboutus(request):
    return HttpResponse("this is about us page")

def contactus(request):
    return HttpResponse("this is about us page")

def services(request):
    return HttpResponse("this is about us page")


