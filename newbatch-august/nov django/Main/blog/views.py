from django.shortcuts import render
from django.http import HttpResponse
from blog.models import ContactUs
# Create your views here.


def home(request):
    # return HttpResponse("this is home page")
    return render(request, "home.html")


def aboutus(request):
    return HttpResponse("this is about us page")

def contactus(request):
    if request.method == "POST":
        nm = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("number")
        message = request.POST.get("msg")

        data = ContactUs(Name = nm, Email = email, Phone_Number = phone, Message = message)
        data.save()


    return render(request, "contact-us.html")

def services(request):
    return HttpResponse("this is about us page")


