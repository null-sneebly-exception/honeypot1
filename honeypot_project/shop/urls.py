from django.urls import path

from . import views

urlpatterns = [
    path('', views.shop, name='shop'),
    path('<str:product_name>/', views.productpage, name='productpage'),
]
