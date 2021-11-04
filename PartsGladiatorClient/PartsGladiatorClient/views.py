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
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt




def index(request):
    template = loader.get_template("index.html")
    #products = Product.objects.all()
    #promotions = Promotions.objects.all()
    #categories = Category.objects.all()
    

    context = {
        #"products": products,
        #"promotions": promotions,
        #"categories": categories,
    }

    return HttpResponse(template.render(context, request))


@csrf_exempt
def contact(request):
    template = loader.get_template("contact.html")
    form = ContactForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            send_mail(
                request.POST['subject'],
                request.POST['message'],
                request.POST['mail'],
                ['1831154@etu.cchic.ca'],
                fail_silently = False,
            )
            return HttpResponseRedirect("/contact")
    
        return HttpResponseRedirect("/contact")
    else:
        context = {
                'form':form
        }

        return HttpResponse(template.render(context, request))



def information(request):
    template = loader.get_template("information.html")


    context = {
        "adress": "Rue Racine",
        "zipCode": "k4e2k0",
        "telephone": "418-123-4567",
    }

    return HttpResponse(template.render(context, request))



def product(request, productId):
    template = loader.get_template("product.html")
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


