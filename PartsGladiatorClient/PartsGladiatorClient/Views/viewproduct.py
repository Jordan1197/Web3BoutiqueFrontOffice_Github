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
from datetime import date, datetime


def allProducts(request):
    template = loader.get_template("product.html")

    context = {
        'categories': PgCategory.objects.all(),
        'promotions': PgPromotion.objects.all(),
        'brands': PgBrand.objects.all(),
        'images': PgImage.objects.all(),
        'scategory': "",
        'sbrand': "",
        'spromotion': "",
        'sname': "",
        'vbrand': "",
        'vpromotion': "",
        'vname': "",
    }

    if request.method == "POST":

        Products = PgProduct.objects.filter(
            name__icontains=request.POST['Name']
        )
        if request.POST['Category'] != "":
            Products = Products.filter(
                categoryid=request.POST['Category']
            )
            cat = get_object_or_404(PgCategory, pk=request.POST['Category'])           
            context['scategory'] = cat.name                   
            context['vcategory'] = cat.id
            
        if request.POST['Brand'] != "":
            Products = Products.filter(
                brandid=request.POST['Brand']
            )
            brand = get_object_or_404(PgBrand, pk=request.POST['Brand'])
            context['vbrand'] = brand.id
            context['sbrand'] = brand.name
            
        if request.POST['Promotion'] != "":
            Products = Products.filter(
                promotionid=request.POST['Promotion']
            )
            promo = get_object_or_404(PgPromotion, pk=request.POST['Promotion'])
            context['vpromotion'] = promo.id
            context['spromotion'] = promo.name

        listeProduit = []
        for product in Products:
            i = 0
            for image in PgImage.objects.all():
                if i == 0:
                    if product.id == image.productid.id:
                        product.createdby = image.path
                        listeProduit.append(product)
                        i = 1

        context['products'] = listeProduit
        context['sname'] = request.POST['Name']
        
        
        
        
        
        
        return HttpResponse(template.render(context, request))
    else:
        listeProduit = []
        AllProds = PgProduct.objects.all()
        AllImages = PgImage.objects.all()

        for product in AllProds:
            i = 0
            for image in AllImages:
                if i == 0:              
                    if product.id == image.productid.id:
                        product.createdby = image.path
                        listeProduit.append(product)
                        i = 1

        context['products'] = listeProduit

    return HttpResponse(template.render(context, request))


def category(request, categoryId):
    template = loader.get_template("category.html")
    Produits = PgProduct.objects.filter(
        categoryid=categoryId
    )

    context = {
        'products': Produits,
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
        'products': Produits,
        'categories': PgCategory.objects.all(),
        'promotions': PgPromotion.objects.all(),
        'brands': PgBrand.objects.all(),
        'images': PgImage.objects.all(),
        'scategory': "",
        'sbrand': "",
        'spromotion': "",
        'sname': "",
        'vbrand': "",
        'vpromotion': "",
        'vname': "",
    }

    return HttpResponse(template.render(context, request))


def details(request, productId):
    template = loader.get_template("details.html")
    Product = get_object_or_404(PgProduct, pk=productId)
    Brand = get_object_or_404(PgBrand, pk=Product.brandid)
    Category = get_object_or_404(PgCategory, pk=Product.categoryid)
    Characteristics = get_object_or_404(
    PgCharacteristic, pk=Product.caracteristicid)
    Attribute = get_object_or_404(PgTypeattribut, pk=Product.attributid)
    AttrValues = PgValeurattribut.objects.all()
    Retailers = get_object_or_404(PgRetailer, pk=Product.retailerid)
    Images = PgImage.objects.all()
    result = Images.filter(productid=Product.id)
    try: 
        PgPromotion.objects.get(id=Product.promotionid)
    except:
        PromoPrice = ''
    else:
        PromoPrice = PgPromotion.objects.get(id=Product.promotionid)
        if PromoPrice.active == 1:
            PromoPrice = Product.price - (PromoPrice.discount / 100) * Product.price
        else:
            PromoPrice = ''

    noquantity= ""
    
    
    if request.method == "POST":
        NewCart = None
        if 'cartid' not in request.session:
            NewCart = PgCart.objects.create(createddate = datetime.now())
            request.session['cartid'] = PgCart.objects.latest('id').id
        
        Cart = PgCart.objects.get(id = request.session['cartid'])
        
        if NewCart != None:
            Cart = NewCart
        
        
        NewProduct = PgProduct.objects.get(id=productId)
        if int(request.POST["qty"]) <= NewProduct.quantity:
            NewOrder = PgCartproduct.objects.create(cartid=Cart,productid=NewProduct,quantity=request.POST["qty"])
            
        else:
            noquantity = "Cette article est en rupture de stock. " + str(NewProduct.quantity)+ " restants"
        
    context = {
        "Product": Product,
        "Name": Product.name,
        "Brand": Brand.name,
        "Category": Category.name,
        "Quantity": Product.quantity,
        "Price": Product.price,
        "Characteristics": Characteristics.name,
        "Attribute": Attribute,
        "AttrValues":AttrValues,
        "Description": Product.description,
        "Retailers": Retailers.name,
        'Images': Images,
        'ProdImg': result,
        'PromoPrice': PromoPrice,
        'noquantity':noquantity,
    }   

    return HttpResponse(template.render(context, request))
