from multiprocessing import context
from django.shortcuts import render
from django.template import loader


# Create your views here.
from django.http import *
from .models import *


shopItems = []



def shop(request):
    product_list = Product.objects.all()
    template = loader.get_template('shop.html')
    context = {'product_list': product_list,}
    return HttpResponse(template.render(context, request))

  
def productpage(request,product_name):
    try:
        product = Product.objects.get(name=product_name)
    except Product.DoesNotExist:
        raise Http404("Product does not exist")
    return HttpResponse(product_name)
    

def shoppingCartPage(request):
    template = loader.get_template('showsession.html')
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
    return HttpResponse("WOOOOOOO")


    
