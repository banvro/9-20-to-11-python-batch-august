from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import  api_view
from hlo.serilizer import ContactusSerilizer
from hlo.models import ContactUs

# Create your views here.
@api_view(["GET"])
def getingdata(request):
    alldata = ContactUs.objects.all().order_by("-id")
    serlizeed_data = ContactusSerilizer(alldata, many = True)
    return Response({
        "Message" : "Data Fetch Sucessfully",
        "Data" : serlizeed_data.data
    })

@api_view(["POST"])
def savethisdata(request):
    datax = ContactusSerilizer(data=request.data)
    if datax.is_valid():
        datax.save()
    return Response({
        "API" : "this is post api",
        "Message" : "data saved suvessfully",
        "data" : datax.data})


@api_view(["POST"])
def detethiddata(request, id):
    obj = ContactUs.objects.get(id = id)
    obj.delete()
    return Response({
        "API" : "this is post api",
        "Message" : "data deleted suvessfully",
  })

@api_view(["PATCH"])
def updatethisdata(request, id):
    obj = ContactUs.objects.get(id = id)
    datax = ContactusSerilizer(obj, data=request.data, partial = True)
    if datax.is_valid():
        datax.save()
    return Response({
        "API" : "this is Patch api",
        "Message" : "data Updated suvessfully",
        "data" : datax.data})