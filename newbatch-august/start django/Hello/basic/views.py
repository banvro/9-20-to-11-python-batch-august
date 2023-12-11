from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def main(request):
    return HttpResponse("this is main page")

def xyz(request):
    return HttpResponse("this is xyz page")


def home(request):
    return render(request, "home.html")


def carfun(request):
    return render(request, "car.html")