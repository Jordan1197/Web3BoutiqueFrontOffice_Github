from email.mime import text
from django import template
from django.db.models.fields import NullBooleanField
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import HttpResponseRedirect
from PartsGladiatorClient.settings import EMAIL_HOST_USER
from PartsGladiatorClient.settings import EMAIL_HOST_PASSWORD
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



user1 = None

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

def cart(request):
    template = loader.get_template("cart.html")

    context = {
        #"products": products,
    }

    return HttpResponse(template.render(context, request))


def page_not_found_view(request, exception):
    return render(request, '404.html',status=404)

def login(request):
    template = loader.get_template('login.html')

    form = request.POST.get('loginform')

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password'].encode("utf-8")
        
        encodedPassword = base64.b64encode(password)
        
        try:
            user = PgClient.objects.get(
                email = username,         
                password = encodedPassword 
                )
            context = {
                'user':user,
            }
            global user1
            user1 =user
            return HttpResponseRedirect("/profil")
        except:
            context = {
                'form':form,
                'errorcred':"Identifiants incorrect."
            }
            return HttpResponse(template.render(context,request))
    else:
        context = {
            'form':form,
        }
        return HttpResponse(template.render(context,request))

def profil(request):
    template = loader.get_template('profil.html')

    context = {
        'user':user1
    }
    return HttpResponse(template.render(context,request))

def createuser(request):
    template = loader.get_template('createuser.html')
    
    form = request.POST.get('createuserform')

    if request.method == "POST":

        prenom = request.POST['prenom']
        nom = request.POST['nom']
        courriel = request.POST['courriel']
        password = request.POST['password'].encode("utf-8")
        encodedPassword = base64.b64encode(password)
        confirmpassword = request.POST['confirmpassword'].encode("utf-8")
        encodedConfirmPassword = base64.b64encode(confirmpassword)        
        pays = request.POST['pays']
        region = request.POST['region']
        ville = request.POST['ville']
        rue = request.POST['rue']
        codepostal = request.POST['zipcode']

        if(encodedPassword == encodedConfirmPassword):
            residence = PgAddress(
                zipcode = codepostal,
                city = ville,
                country = pays,
                state = region,
                street = rue,
                createddate = datetime.now(),
                createdby = "default",
                lastupdateddate = date.min,
                lastupdatedby = "default",
                deleteddate = date.min,
                deletedby = "default",
            )
            residence.save()

            client = PgClient(
                lastname = nom,
                firstname = prenom,
                email = courriel,
                password = encodedPassword,
                addressid = residence.id,
                createddate =datetime.now(),
                createdby = "default",
                lastupdateddate =date.min,
                lastupdatedby = "default",
                deleteddate = date.min,
                deletedby = "null",
            )
            client.save()
            
            mail_content = "Bienvenue cher membre gladiator, vous êtes désormais autorisé à magasiner les pièces de vos rêves ! Merci de nous avoir choisi."
            sender_address = EMAIL_HOST_USER
            send_pass = EMAIL_HOST_PASSWORD
            receiver_address = client.email
            #setup MIME
            message = MIMEMultipart()
            message['From'] = sender_address
            message['To'] = receiver_address
            message['Subject'] = "Félicitation pour la création de votre compte ! :)"
            #le message
            message.attach(MIMEText(mail_content, 'plain'))
            #session smtp
            session = smtplib.SMTP('smtp.gmail.com',587)
            session.starttls()
            session.login(sender_address,send_pass)
            text = message.as_string()
            session.sendmail(sender_address,receiver_address,text)
            session.quit()

            return HttpResponseRedirect("/connexion")

        else:
            context = {
                'passwordinvalide':"les mots de passe ne corresponde pas."
            } 
            return HttpResponse(template.render(context,request))
        


        
        

    else:
        context = {
            'form':form,
        }

        return HttpResponse(template.render(context,request))