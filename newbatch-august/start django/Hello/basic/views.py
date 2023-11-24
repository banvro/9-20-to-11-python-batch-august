from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def main(request):
    return HttpResponse("this is main page")

def xyz(request):
    return HttpResponse("this is xyz page")