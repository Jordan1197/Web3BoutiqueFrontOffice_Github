from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import HttpResponseRedirect
from PartsGladiatorClient.forms import *
from django.template import loader
from django.http import HttpResponse, HttpResponseNotFound
from django.views.decorators.http import require_http_methods
from django.template import RequestContext
from PartsGladiatorClient.Models.models import *
from django.shortcuts import get_object_or_404


def allProducts(request):
    template = loader.get_template("product.html")
    Produits = Product.objects.all()

    context = {
        'products': Produits
    }
    return HttpResponse(template.render(context, request))



def category(request, categoryId):
    template = loader.get_template("category.html")
    Produits = Product.objects.filter(
        CategoryId=categoryId
    )

    context = {
        'products': Produits
    }
    
    return HttpResponse(template.render(context, request))



def brand(request, brandId):
    template = loader.get_template("product.html")
    Produits = Product.objects.filter(
        PromotionId=promoId
    )

    context = {
        'products': Produits
    }

    return HttpResponse(template.render(context, request))


def promotion(request, promoId):
    template = loader.get_template("product.html")
    Produits = Product.objects.filter(
        PromotionId=promoId
    )

    context = {
        'products': Produits
    }

    return HttpResponse(template.render(context, request))


def search(request):
    template = loader.get_template("product.html")
    form = SearchForm(request.POST)

    if request.method == 'POST':
         
        Produits = PgProduct.objects.filter(
            name=request.POST['Name']
        ).filter(
            categoryid=request.POST['Category']
        ).filter(
            caracteristicid=request.POST['Characteristic']
        ).filter(
            brandid=request.POST['Brand']
        ).filter(
            promotionid=request.POST['Promotion']
        )    
        
        context = {
            'products': Produits,
            'form':form
        }
        return HttpResponseRedirect("/product/search")
    else:
            
        context = {
            'products': PgProduct.objects.all(),
            'categories': PgCategory.objects.all(),
            'promotions': PgPromotion.objects.all(),
            'brands': PgBrand.objects.all(),
            'characteristics': PgCharacteristic.objects.all(),
            'form': form,
        }

    return HttpResponse(template.render(context, request)) 


def details(request, productId):
    template = loader.get_template("details.html")
    Product = get_object_or_404(Product, pk=productId)
    
    context = {
        "Name": Product.Name,
        "Brand": Product.Brand.Name,
        "Category": Product.Category.Name,
        "Quantity": Product.Quantity,
        "Price": Product.Price,
        "Characteristics": Product.Characteristics,
        "Attribute": Product.Attribute,
        "Description": Product.Description,
        "Images": Product.Images,
        "Retailers": Product.Retailers,
    }

    return HttpResponse(template.render(context, request))


