from multiprocessing import context
from re import template
from urllib.request import HTTPRedirectHandler
from django.shortcuts import render,redirect
from django.template import loader
from django.http import HttpResponseRedirect
import datetime
import logging
import requests
from django.contrib.auth import authenticate, login as user_login, logout as user_logout
from time import sleep


# Create your views here.
from django.http import *
from .models import *

logger = logging.getLogger(__name__)
logging.basicConfig(filename='shop.log', encoding='utf-8', level=logging.DEBUG)
shopItems = []

def shop(request):
    product_list = Product.objects.all()
    template = loader.get_template('index.html')
    context = {'product_list': product_list,}
    if request.method=="POST":
        data=request.POST
        url = data.get("url")
        if url == "http://52.201.246.164/shop/":
            return redirect("/shop")
        req = requests.get(url = url)
        #crafts new HTTP response object out of the content of req from python requests library, and return to browser.
        #if user changes url in html form , they can make server render malicious site, or a resource behind the firewall
        try:
            django_formatted_response = HttpResponse(
            content=req.content)
        except:
            sleep(2)
            django_formatted_response = HttpResponse(
            content=req.content)
        if url == 'http://52.201.246.146/shop':
            return redirect("/shop")
        if url != 'http://52.201.246.146/shop/':
            logger.critical('XXS Forgery Warning!!!!! IP OF REQUESTER: '+request.META['REMOTE_ADDR'])
            logger.critical('Bad content returned ='+ req.text)
            return django_formatted_response
    request.META["REMOTE_ADDR"]  
    return HttpResponse(template.render(context, request))

  
def productpage(request,product_name):
    template = loader.get_template('product.html')
    if request.method=="POST":
        data=request.POST
        comment=data.get("comment")
        name = data.get("name")
        product = data.get("product")
        substring = "<script>"
        if substring in comment:
            logger.critical('XSS Forgery Warning. Malicious string = '+ comment +' IP OF REQUESTER: '+request.META['REMOTE_ADDR'])
        x =Comment(product=product,poster=name,date=datetime.now(),comment=comment)
        x.save()
    comment_list = Comment.objects.filter(product=product_name)
    try:
        product = Product.objects.get(name=product_name)
        context= {"product_info":product,'comment_list':comment_list,}
    except Product.DoesNotExist:
        raise Http404("Product does not exist")
    return HttpResponse(template.render(context,request))
    

def shoppingCartPage(request):
    template = loader.get_template('cart.html')
    if request.method == "POST":
        data = request.POST
        if data.get("target") == "inc-dec":
            shoppingcartinc = data.get("shoppingcartinc")
            productname = data.get("productname")
            if shoppingcartinc == "add":
                request.session['shopping_cart'][productname]=(request.session['shopping_cart'][productname]+1)
            if shoppingcartinc == "subtract":
                request.session['shopping_cart'][productname] = (request.session['shopping_cart'][productname]-1)
                if request.session['shopping_cart'][productname] == 0:
                    del request.session['shopping_cart'][productname]
        if data.get("target") == "remove":
            productname = data.get("productname")
            del request.session['shopping_cart'][productname]
    try:
        cart=request.session['shopping_cart']
    except KeyError:
        request.session['shopping_cart']={}
        cart=request.session['shopping_cart']   
    products = Product.objects.all()
    context={'shopping_cart':cart,"products": products}
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

def checkout(request):
    if request.user.is_authenticated:
        return(HttpResponse("Authenticated checkout"))
    else:
        return(HttpResponse("CHECKOUT HERE"))

def login(request):
    context = {}
    template = loader.get_template("login.html")
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username,password = password)
        logger.critical(user)
        if user is not None:
            user_login(request,user)
            return(HttpResponseRedirect("/shop"))
        else:
            context={"message":"<script>alert(\"invalid credentials\")</script>"}
            logger.critical('Invalid Credentials. IP OF REQUESTER: '+request.META['REMOTE_ADDR'] + 'Username used: '+username)
            return(HttpResponse(template.render(context,request)))
    return(HttpResponse(template.render(context,request)))


def logout(request):
    user_logout(request)
    return(HttpResponseRedirect("/shop"))
    
class AllowUnsafeRedirect(HttpResponsePermanentRedirect):
    allowed_schemes = ['file',"http","https"]
