from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignUpForm
from PartsGladiatorClient.Models.models import *
from datetime import date,datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from PartsGladiatorClient.settings import EMAIL_HOST_USER
from PartsGladiatorClient.settings import EMAIL_HOST_PASSWORD
import base64

# Create your views here.
def home(request):
    return render(request, 'index.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            residence = PgAddress(
                zipcode = form.cleaned_data.get('zipcode'),
                city = form.cleaned_data.get('ville'),
                country = form.cleaned_data.get('pays'),
                state = form.cleaned_data.get('region'),
                street = form.cleaned_data.get('rue'),
                createddate = datetime.now(),
                createdby = "default",
                lastupdateddate = date.min,
                lastupdatedby = "default",
                deleteddate = date.min,
                deletedby = "default",
            )            
            residence.save()

            user = form.save()
            pwd = form.cleaned_data.get('password1').encode("utf-8")
            encodedPassword = base64.b64encode(pwd)
            client = PgClient(
                lastname = form.cleaned_data.get('lastname'),
                firstname = form.cleaned_data.get('firstname'),
                email = form.cleaned_data.get('email'),
                password = encodedPassword,
                addressid = residence.id,
                createddate =datetime.now(),
                createdby = "default",
                lastupdateddate =date.min,
                lastupdatedby = "default",
                deleteddate = date.min,
                deletedby = "null",
            )
            #save dans la table client
            client.save()
            user.addressid = residence.id
            user.createddate = datetime.now()
            user.lastupdateddate = datetime.min
            user.deleteddate = datetime.min
            user.createdby = "default"
            user.deletedby = "default"
            user.lastupdatedby = "default"
            #save dans la table authen_customuser
            user.save()
            
            

            #MAIL
            mail_content = "Bienvenue cher membre gladiator, vous êtes désormais autorisé à magasiner les pièces de vos rêves ! Merci de nous avoir choisi."
            sender_address = EMAIL_HOST_USER
            send_pass = EMAIL_HOST_PASSWORD
            receiver_address = user.email
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

            #LOGIN
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'createuser.html', { 'form' : form })