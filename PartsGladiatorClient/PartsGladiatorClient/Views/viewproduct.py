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
from django.db.models.functions import *


def allProducts(request):
    template = loader.get_template("product.html")
    form = SearchForm(request.POST)

    if request.method == 'POST':

        Produits = PgProduct.objects.all()

        if request.POST['Name'] != "":
            Produits.filter(
                name=request.POST['Name']
            )
        if request.POST['Category'] != "":
            Produits.filter(
                categoryid=request.POST['Category']
            )
        if request.POST['Characteristic'] != "":
            Produits.filter(
                caracteristicid=request.POST['Characteristic']
            )
        if request.POST['Brand'] != "":
            Produits.filter(
                brandid=request.POST['Brand']
            )
        if request.POST['Promotion'] != "":
            Produits.filter(
                promotionid=request.POST['Promotion']
            )

        context = {
            'products': Produits,
            'form': form,
        }
        return HttpResponseRedirect("/product")
    else:
        
        context = {
            'products': PgProduct.objects.all(),
            'categories': PgCategory.objects.all(),
            'promotions': PgPromotion.objects.all(),
            'brands': PgBrand.objects.all(),
            'characteristics': PgCharacteristic.objects.all(),
            'form': form,
            'images': PgImage.objects.all(),

        }

    return HttpResponse(template.render(context, request))


def category(request, categoryId):
    template = loader.get_template("category.html")
    Produits = PgProduct.objects.filter(
        categoryid=categoryId
    )

    context = {
        'products': Produits
    }

    return HttpResponse(template.render(context, request))


def brand(request, brandId):
    template = loader.get_template("product.html")
    Produits = PgProduct.objects.filter(
        brandid=brandId
    )

    context = {
        'products': Produits
    }

    return HttpResponse(template.render(context, request))


def promotion(request, promoId):
    template = loader.get_template("product.html")
    Produits = PgProduct.objects.filter(
        promotionid=promoId
    )

    context = {
        'products': Produits
    }

    return HttpResponse(template.render(context, request))


def details(request, productId):
    template = loader.get_template("details.html")
    Product = get_object_or_404(PgProduct, pk=productId)

    context = {
        "Name": Product.name,
        "Brand": Product.brand.name,
        "Category": Product.category.name,
        "Quantity": Product.Quantity,
        "Price": Product.Price,
        "Characteristics": Product.Characteristics,
        "Attribute": Product.Attribute,
        "Description": Product.Description,
        "Images": Product.Images, # faire une liste qui laisse une image par product
        "Retailers": Product.Retailers,
    }

    return HttpResponse(template.render(context, request))
