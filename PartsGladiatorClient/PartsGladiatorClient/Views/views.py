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
from PartsGladiatorClient.Models import models
import math



def index(request):
    template = loader.get_template("index.html")
    promotions = PgPromotion.objects.filter(
        active = 1
    ).order_by('name').order_by('startdate')[:9]
    produitpromoFromView = prodpromoviews.objects.all()[:9]
    produitFromViews = OneImageProductViews.objects.all()[:9]

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

def cart(request):
    template = loader.get_template("cart.html")
    AllImages = PgImage.objects.all()
    if request.method == "POST":
        Product = PgCartproduct.objects.filter(id=request.POST["remove"])        
        Product.delete()

            
    host = request.get_host()
    listeProduit = []
    nbArticle = 0
        
    if 'cartid' in request.session:
        CartProducts = PgCartproduct.objects.filter(cartid=request.session['cartid'])
            
        for product in CartProducts:
                 	
            NewProduct = PgProduct.objects.get(id=product.productid.id)
            NewProduct.quantity = product.quantity
            NewProduct.brandid = NewProduct.price            
            NewProduct.categoryid = product.id #jo remove productid si marche pas
            i =0
            for image in AllImages:
                if i == 0:              
                    if NewProduct.id == image.productid.id:
                        NewProduct.createdby = image.path
                        
                        i = 1   
            try: 
                PgPromotion.objects.get(id=NewProduct.promotionid)
            except:
                PromoPrice = ''
            else:
                PromoPrice = PgPromotion.objects.get(id=NewProduct.promotionid)
                if PromoPrice.active == 1:
                    PromoPrice = NewProduct.price - (PromoPrice.discount / 100) * NewProduct.price
                else:
                    PromoPrice = ''
                NewProduct.price = PromoPrice
                
            nbArticle += 1
            listeProduit.append(NewProduct)
        
        
                
    prix = 0
    n = ""
    for p in listeProduit:
        prix = (p.price * p.quantity) + prix
        n = p.name = " "
                                                
    taxes = prix * 0.05
        
    paypal_dict = {
        'business': PAYPAL_RECEIVER_EMAIL ,
        'amount': prix,#ajouter le prix du panier ici
        'item_name': n,
        'tax':taxes,
        'currency_code': 'CAD',
        'notify_url': 'http://{}{}'.format(host,
                                        reverse('paypal-ipn')),
        'return_url': 'http://{}{}'.format(host,
                                        reverse('payment_done')),
        'cancel_return': 'http://{}{}'.format(host,
                                            reverse('payment_canceled')),
                                                
    }
    form = PayPalPaymentsForm(initial=paypal_dict)
    
    
    context = {
        "product": listeProduit,
        'form':form,
        'price':prix,
        'nbArticle':nbArticle,        
    }

    return HttpResponse(template.render(context, request))

       

@csrf_exempt
def payment_done(request):
    loader.get_template("payment_done.html")
    host = request.get_host()
    user = CustomUser.objects.get(id=request.user.id) 
    CartProducts = PgCartproduct.objects.filter(cartid=request.session['cartid'])
    
    listeProduit = []
	
    for product in CartProducts: 
        newprod = PgProduct.objects.get(id = product.productid.id)

        newprod.quantity = newprod.quantity - product.quantity
        newprod.save()

        newprod.quantity = product.quantity
        try: 
            PgPromotion.objects.get(id=newprod.promotionid)
        except:
            PromoPrice = ''
        else:
            PromoPrice = PgPromotion.objects.get(id=newprod.promotionid)
            if PromoPrice.active == 1:
                PromoPrice = newprod.price - (PromoPrice.discount / 100) * newprod.price
            else:
                PromoPrice = ''
            newprod.price = PromoPrice

        listeProduit.append(newprod)

    prix =0
    taxes=0
    for p in listeProduit:
        prix = (p.price * p.quantity)+prix
        
        
        
                                              
    taxes = prix * 0.05
    prixwithtaxe = prix+taxes

    #MAIL
    mail_content = "félicitation pour votre achat !"
    sender_address = EMAIL_HOST_USER
    send_pass = EMAIL_HOST_PASSWORD
    receiver_address = user.email
    #setup MIME
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = "félicitation pour votre achat !"
    #le message
    message.attach(MIMEText(mail_content, 'plain'))
    #session smtp
    session = smtplib.SMTP('smtp.gmail.com',587)
    session.starttls()
    session.login(sender_address,send_pass)
    text = message.as_string()
    session.sendmail(sender_address,receiver_address,text)
    session.quit()

    
    AllProds = listeProduit
    listeProduit  = []
    AllImages = PgImage.objects.all()

    for product in AllProds:
        i = 0
        for image in AllImages:
            if i == 0:              
                if product.id == image.productid.id:
                    product.createdby = image.path
                    listeProduit.append(product)
                    i = 1

   
    
                
                

    context = {
        'products':listeProduit,
        'user':user,
        'images': PgImage.objects.all(),
        'cartproduct':CartProducts,
        'prix':prix,
        'taxes':taxes,
        'prixwithtaxe':prixwithtaxe,
    }            

    return render(request, 'payment_done.html',context)


@csrf_exempt
def payment_canceled(request):
    return render(request, 'payment_canceled.html')


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


