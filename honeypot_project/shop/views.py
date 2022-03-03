from multiprocessing import context
from urllib.request import HTTPRedirectHandler
from django.shortcuts import render,redirect
from django.template import loader
from django.http import HttpResponseRedirect


# Create your views here.
from django.http import *
from .models import *


shopItems = []


def shop(request):
    product_list = Product.objects.all()
    template = loader.get_template('index.html')
    context = {'product_list': product_list,}
    if request.method=="POST":
        data=request.POST
        return AllowUnsafeRedirect(data.get("url"))
        
        
    return HttpResponse(template.render(context, request))

  
def productpage(request,product_name):
    template = loader.get_template('productpage.html')
    try:
        product = Product.objects.get(name=product_name)
        context= {"product_info":product}
    except Product.DoesNotExist:
        raise Http404("Product does not exist")
    return HttpResponse(template.render(context,request))
    

def shoppingCartPage(request):
    template = loader.get_template('showsession.html')
    try:
        cart=request.session['shopping_cart']
    except KeyError:
        request.session['shopping_cart']={}
        cart=request.session['shopping_cart']   

    context={'shopping_cart':cart}
    return HttpResponse(template.render(context,request))



def addtocart(request,product_name):
    try:
        foo = request.session['shopping_cart']
    except KeyError:
        request.session['shopping_cart']={}   
    try:
        foo = request.session['shopping_cart'][product_name]
    except KeyError:
        request.session['shopping_cart'][product_name] = 0
    request.session['shopping_cart'][product_name]= int(request.session['shopping_cart'][product_name])+1
    return redirect("/shop")


    
class AllowUnsafeRedirect(HttpResponsePermanentRedirect):
    allowed_schemes = ['file',"http","https"]