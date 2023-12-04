from django.shortcuts import render, redirect
from blog.models import SaveDetail
# Create your views here.

def home(request):
    return render(request, "home.html")


def suaveinfo(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        number = request.POST.get("number")
        message = request.POST.get("msg")
       
        data = SaveDetail(Name = name, Phone_Number = number, Email = email, message = message )
        data.save()
        return redirect("home")