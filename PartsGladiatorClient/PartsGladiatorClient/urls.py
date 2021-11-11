"""PartsGladiatorClient URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from PartsGladiatorClient.Views import viewproduct
from PartsGladiatorClient.Views import views

urlpatterns = [
    path('', views.index),
    path('product', viewproduct.allProducts),
    path('product/<int:productId>', viewproduct.details),
    path('product/category/<int:categoryId>', viewproduct.category),
    path('product/brand/<int:brandId>', viewproduct.brand),
    path('product/promotion/<int:promoId>', viewproduct.promotion),
    path('product/search', viewproduct.search), #utiliser slug ou str pour string
    path('contact', views.contact),
    path('information', views.information),
    path('cart',views.cart),
    path('about',views.about)
    
]
