from multiprocessing import context
from urllib.request import HTTPRedirectHandler
from django.shortcuts import render,redirect
from django.template import loader
from django.http import HttpResponseRedirect
import datetime
import logging


# Create your views here.
from django.http import *
from .models import *


logger = logging.getLogger(__name__)


shopItems = []


def shop(request):
    product_list = Product.objects.all()
    template = loader.get_template('index.html')
    context = {'product_list': product_list,}
    if request.method=="POST":
        data=request.POST
        return AllowUnsafeRedirect(data.get("url"))
        
    logger.error(request.META['REMOTE_ADDR'])

    return HttpResponse(template.render(context, request))

  
def productpage(request,product_name):
    template = loader.get_template('productpage.html')
    if request.method=="POST":
        data=request.POST
        comment=data.get("comment")
        name = data.get("name")
        product = data.get("product")
        x =Comment(product=product,poster=name,date=datetime.datetime.now(),comment=comment)
        x.save()

    if name != 'http://127.0.0.1:8000/shop/':
        logger.error('XXS Forgery Warning')

    comment_list = Comment.objects.filter(product=product_name)

    try:
        product = Product.objects.get(name=product_name)
        context= {"product_info":product,'comment_list':comment_list,}
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
