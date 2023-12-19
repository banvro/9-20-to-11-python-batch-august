from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def set_session(request):
    request.session["username"] = "kriss moris"
    return HttpResponse("session set")

def get_sessionn(request):
    zx = request.session.get("username")
    return HttpResponse(f"The value of username is : {zx}")

def dlt_session(request):
    del request.session["uername"]
    return HttpResponse("session deleted")



# cookies

def set_cookies(request):
    responce = HttpResponse("Cookies is set")
    responce.set_cookie("mycookie", "hlo world", max_age=3600)
    return responce


def get_cookies(request):
    zx = request.COOKIES.get("mycookie")
    return HttpResponse(f"cookie value is : {zx}")


def del_cookies(request):
    responce = HttpResponse("Cookies is set")
    responce.set_cookie("mycookie", "", max_age=3600)
    return responce
