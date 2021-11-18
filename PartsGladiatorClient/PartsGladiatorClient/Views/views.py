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
from django.conf import settings




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