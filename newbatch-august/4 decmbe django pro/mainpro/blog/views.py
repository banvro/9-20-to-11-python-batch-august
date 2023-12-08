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
        return redirect("show")

 

def showthisdta(request):
    data = SaveDetail.objects.all()
    return render(request, "showdata.html", {"mydata" : data})

# ORM 


def deletethis(request, myid):
    # print(myid, "xxxxxxxxxxxxxxxxxxxxxxxx")
    data = SaveDetail.objects.get(id = myid)
    data.delete()

    return redirect("show")



def updatedata(request, x):
    data = SaveDetail.objects.get(id = x)
    print(data, "xxxxxxxx")
    return render(request, "updatethisdata.html", {"senddata" : data})


def updatenow(request, id):
    data = SaveDetail.objects.get(id = id)

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        number = request.POST.get("number")
        message = request.POST.get("msg")

        
        data.Name = name
        data.Email = email
        data.Phone_Number = number
        data.message = message

        data.save()


    return redirect("show")