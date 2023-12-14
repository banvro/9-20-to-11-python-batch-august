from django.shortcuts import render, redirect
from todo.models import TodoData

# Create your views here.

def home(request):
    alltodos = TodoData.objects.all()

    return render(request, "home.html", {"todos" : alltodos, "check" : "home"})


def savethistodo(request):
    if request.method == "POST":
        title = request.POST.get("title")
        dec = request.POST.get("dec")

        mydata = TodoData(title = title, desc = dec)
        mydata.save()
    return redirect("home")


def deletethis(request, myid):
    todo = TodoData.objects.get(id = myid)
    todo.delete()
    return redirect("home")


def updatetodo(request, myid):
    alltodos = TodoData.objects.all()
    mytodo = TodoData.objects.get(id = myid)
    mydict = {"todos" : alltodos, "check" : "update", "todo" : mytodo}
    return render(request, "home.html", mydict)


def updatethisnow(request, myid):
    mytodo = TodoData.objects.get(id = myid)
    if request.method == "POST":
        name = request.POST.get("title")
        dec = request.POST.get("dec")

        mytodo.title = name
        mytodo.desc = dec

        mytodo.save()

    return redirect("home")