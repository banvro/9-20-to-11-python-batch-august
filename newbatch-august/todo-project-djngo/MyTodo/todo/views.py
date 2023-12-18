from django.shortcuts import render, redirect
from todo.models import TodoData
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def home(request):
    alltodos = TodoData.objects.all()

    return render(request, "home.html", {"todos" : alltodos, "check" : "home"})


def savethistodo(request):
    if request.method == "POST":
        title = request.POST.get("title")
        dec = request.POST.get("dec")
        img = request.FILES.get("myimg")

        # print(img, "yyyyyyyy")

        mydata = TodoData(title = title, desc = dec, My_Image = img)
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



def signupgere(request):
    if request.method == "POST":
        usernmae = request.POST.get("username")
        email = request.POST.get("email")
        fname = request.POST.get("name")
        password = request.POST.get("passw")

        userx = User.objects.create_user(username = usernmae, first_name = fname, email = email, password=password)
        userx.save()

    return redirect("home")

def loginfun(request):
    if request.method == "POST":
        usern = request.POST.get("username")
        passw = request.POST.get("password")

        check = authenticate(username = usern, password = passw)

        if check is not None:
            login(request, check)


    return redirect("home")


def logouthere(request):
    logout(request)

    return redirect("home")