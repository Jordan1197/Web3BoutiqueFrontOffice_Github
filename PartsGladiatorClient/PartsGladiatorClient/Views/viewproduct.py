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
    
    context = {
        'categories': PgCategory.objects.all(),
        'promotions': PgPromotion.objects.all(),
        'brands': PgBrand.objects.all(),
        'images': PgImage.objects.all(),
    }

    if request.method == "POST":

               
        Products = PgProduct.objects.filter(
            name__contains=request.POST['Name']
        )
        if request.POST['Category'] != "":
            Products.filter(
                categoryid=request.POST['Category']
            )
        if request.POST['Brand'] != "":
            Products.filter(
                brandid=request.POST['Brand']
            )
        if request.POST['Promotion'] != "":
            Produits.filter(
                promotionid=request.POST['Promotion']
            )

        context['products'] = Products

        return HttpResponse(template.render(context, request))
    else:
        context['products'] = PgProduct.objects.all()
        

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
    Brand = get_object_or_404(PgBrand, pk=Product.brandid)
    Category = get_object_or_404(PgCategory, pk=Product.categoryid)
    Characteristics = get_object_or_404(PgCharacteristic, pk=Product.caracteristicid)
    Attribute = get_object_or_404(PgTypeattribut, pk=Product.attributid)
    Retailers = get_object_or_404(PgRetailer, pk=Product.retailerid)

    context = {
        "Name": Product.name,
        "Brand": Brand.name,
        "Category": Category.name,
        "Quantity": Product.quantity,
        "Price": Product.price,
        "Characteristics": Characteristics.name,
        "Attribute": Attribute.attribut,
        "Description": Product.description,
        "Retailers": Retailers.name,
        'images': PgImage.objects.all(),
    }

    return HttpResponse(template.render(context, request))
