from email.mime import text
import re
from django import template
from django.db.models.fields import NullBooleanField
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import HttpResponseRedirect
from PartsGladiatorClient.settings import EMAIL_HOST_USER
from PartsGladiatorClient.settings import EMAIL_HOST_PASSWORD
from PartsGladiatorClient.settings import PAYPAL_RECEIVER_EMAIL
from PartsGladiatorClient.forms import *
from django.template import loader
from django.http import HttpResponse, HttpResponseNotFound
from django.views.decorators.http import require_http_methods
from django.template import RequestContext
from PartsGladiatorClient.Models.models import *
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from datetime import date, datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import base64
import smtplib
from authen.models import CustomUser
from django.views.generic import FormView
from django.urls import reverse
from paypal.standard.forms import PayPalPaymentsForm
from django.views.generic import TemplateView
from paypal.standard.models import ST_PP_COMPLETED
from paypal.standard.ipn.signals import valid_ipn_received



def index(request):
    template = loader.get_template("index.html")
    promotions = PgPromotion.objects.filter(
        active = 1
    )
    produitpromoFromView = prodpromoviews.objects.all()
    produitFromViews = OneImageProductViews.objects.all()

    context = {                
        "produitFromViews":produitFromViews,
        "produitpromoFromView":produitpromoFromView,
        "promotions":promotions
    }

    return HttpResponse(template.render(context, request))

def about(request):
    template = loader.get_template("about.html")

    return HttpResponse(template.render())

@csrf_exempt
def contact(request):
    template = loader.get_template("contact.html")
    form = request.POST.get('contactForm')
    if request.method == "POST":
        
        subject = request.POST['subject']
        message = request.POST['message'] +'\n'+ request.POST['mail']
        email_from = request.POST['mail']
        recipient_list = ['partgaldiator@gmail.com']

        send_mail(subject, message, email_from, recipient_list)
        context = {
            "SendingMessage": "Votre message à bien été envoyé merci !!"
        }
        return HttpResponse(template.render(context,request))
    
       
    else:
        context = {
                'form':form,
                
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

def cart(request, userid):
    template = loader.get_template("cart.html")
     host = request.get_host()
    paypal_dict = {
        'business': PAYPAL_RECEIVER_EMAIL ,
        'amount': '1',#ajouter le prix du panier ici
        'item_name': 'Item_Name_xyz',
        'invoice': 'Test Payment Invoice',
        'currency_code': 'USD',
        #'return_url':'',
        'cancel_return': '/cart',
                                              
    }
    form = PayPalPaymentsForm(initial=paypal_dict)
    Cart = PgCart.objects.get(clientid=userid)
    CartProducts = Cartproduct.objects.get(cartid=Cart.id)
    
    listeProduit = []
	
    for product in CartProducts: 
        listeProduit.append(PgProduct.objects.get(id=product.productid))


                                              
    }
    form = PayPalPaymentsForm(initial=paypal_dict)
    
    context = {
        "products": listeProduit,
        'form':form,
    }

    return HttpResponse(template.render(context, request))


def page_not_found_view(request, exception):
    return render(request, '404.html',status=404)


def profil(request,userid):
    template = loader.get_template('profil.html')
    form = request.POST.get('profiluser')
    u = CustomUser.objects.get(id = userid)
    address = PgAddress.objects.get(id = u.addressid)
    if request.method == "POST":
        #modif address
        address.zipcode = request.POST['zipcode']
        address.city = request.POST['ville']
        address.country = request.POST['pays']
        address.state = request.POST['region']
        address.street = request.POST['rue']
        address.lastupdatedate = datetime.now()

        address.save()
        #modif user
        if request.POST['password'] != "":
            u.set_password(request.POST['password'])
            u.username = request.POST['username']
            u.firstname = request.POST['prenom']
            u.lastname = request.POST['nom']
            u.email = request.POST['courriel']

            u.lastupdateddate = datetime.now()
            u.save()
            

            return redirect("home")

        else:
            u.username = request.POST['username']
            u.firstname = request.POST['prenom']
            u.lastname = request.POST['nom']
            u.email = request.POST['courriel']

            u.lastupdateddate = datetime.now()
            u.save()
            
            return redirect("home")

    else:
        context = {
            'form':form,
            'address':address
        }

        return HttpResponse(template.render(context,request))


