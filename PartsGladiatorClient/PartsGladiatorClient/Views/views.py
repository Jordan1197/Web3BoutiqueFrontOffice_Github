from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import HttpResponseRedirect
from Prototype.forms import *
from django.template import loader
from django.http import HttpResponse, HttpResponseNotFound
from django.views.decorators.http import require_http_methods
from django.template import RequestContext
from Prototype.models import *
from django.shortcuts import get_object_or_404


def index(request):
    template = loader.get_template("index.html")


    context = {
        
    }

    return HttpResponse(template.render(context, request))



def contact(request):
    template = loader.get_template("contact.html")


    context = {
        
    }

    return HttpResponse(template.render(context, request))



def information(request):
    template = loader.get_template("information.html")


    context = {
        
    }

    return HttpResponse(template.render(context, request))



def product(request, productId):
    template = loader.get_template("product.html")


    context = {
        
    }

    return HttpResponse(template.render(context, request))


