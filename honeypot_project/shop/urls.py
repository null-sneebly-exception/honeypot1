from django.urls import path

from . import views

urlpatterns = [
    path('', views.shop, name='shop'),
    path('shoppingcart/', views.shoppingCartPage, name='shoppingCartPage'),
    path('<str:product_name>/', views.productpage, name='productpage'),
    path('<str:product_name>/addtocart/', views.addtocart, name='addtocart'),
    
    


]
