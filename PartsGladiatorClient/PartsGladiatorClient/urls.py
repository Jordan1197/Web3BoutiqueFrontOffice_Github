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
from PartsGladiatorClient import Views
from django.contrib.auth import views as auth_views
from authen import views

urlpatterns = [
    path('', Views.views.index, name='home'),
    path('products', viewproduct.allProducts),
    path('product/<int:productId>', viewproduct.details),
    path('product/category/<int:categoryId>', viewproduct.category),
    path('product/brand/<int:brandId>', viewproduct.brand),
    path('product/promotion/<int:promoId>', viewproduct.promotion),
    path('contact', Views.views.contact),
    path('information', Views.views.information),
    path('cart/<int:userid>',Views.views.cart),
    path('about',Views.views.about),
    path('login/',auth_views.LoginView.as_view(template_name='login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(), name='logout'),
    path('createuser/', views.signup, name='signup'),
    path('profil/<int:userid>',Views.views.profil),
    
]

handler404 = "PartsGladiatorClient.Views.views.page_not_found_view"
