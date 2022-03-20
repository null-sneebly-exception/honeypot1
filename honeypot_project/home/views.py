from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def home(request):
    context ={
    "bodytext":"this is our lovely home page"
    }
    return render(request,"home.html",context)

def aboutus(request):
    request.session['test'] = 'cart'
    foo = request.session['test']
    context ={
    "name":"ash",
    "bodytext":"this is our aboutus page",
    "session" : foo
    }
    return render(request,"about.html",context)
