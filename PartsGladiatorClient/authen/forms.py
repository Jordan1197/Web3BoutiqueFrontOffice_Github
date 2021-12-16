from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import fields

from authen.models import CustomUser

class SignUpForm(UserCreationForm):
    prenom= forms.CharField(max_length=100,help_text="Requis.")
    nom= forms.CharField(max_length=100,help_text="Requis.")
    
    email= forms.CharField(max_length=100,help_text="Requis.")
    
    pays = forms.CharField(max_length=100,help_text="Requis.")
    region = forms.CharField(max_length=100,help_text="Requis.")
    ville = forms.CharField(max_length=100,help_text="Requis.")
    rue = forms.CharField(max_length=100,help_text="Requis.")
    zipcode = forms.CharField(max_length=100,help_text="Requis.")

    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('prenom','nom', 'email','pays','region','ville','rue','zipcode')