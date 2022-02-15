from django.shortcuts import render
from django.template import loader


# Create your views here.
from django.http import *
from .models import *


def shop(request):
    product_list = Product.objects.all()
    template = loader.get_template('home.html')
    context = {'product_list': product_list,}
    #return HttpResponse("Welcome to our lovely store")
    return HttpResponse(template.render(context, request))

  
def productpage(request,product_name):
    try:
        product = Product.objects.get(name=product_name)
    except Product.DoesNotExist:
        raise Http404("Product does not exist")
    return HttpResponse(product_name)

