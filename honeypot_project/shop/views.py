from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def shop(request):
    return HttpResponse("Welcome to our lovely store")
