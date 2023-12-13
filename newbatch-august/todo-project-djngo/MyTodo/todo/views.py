from django.shortcuts import render, redirect
from todo.models import TodoData

# Create your views here.

def home(request):
    alltodos = TodoData.objects.all()

    return render(request, "home.html", {"todos" : alltodos})


def savethistodo(request):
    if request.method == "POST":
        title = request.POST.get("title")
        dec = request.POST.get("dec")

        mydata = TodoData(title = title, desc = dec)
        mydata.save()
    return redirect("home")