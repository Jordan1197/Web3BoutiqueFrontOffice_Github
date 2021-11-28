from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import fields

from authen.models import CustomUser

class SignUpForm(UserCreationForm):
    firstname= forms.CharField(max_length=100,help_text="Required.")
    lastname= forms.CharField(max_length=100,help_text="Required.")
    
    email= forms.CharField(max_length=100,help_text="Required.")
    
    pays = forms.CharField(max_length=100,help_text="Required.")
    region = forms.CharField(max_length=100,help_text="Required.")
    ville = forms.CharField(max_length=100,help_text="Required.")
    rue = forms.CharField(max_length=100,help_text="Required.")
    zipcode = forms.CharField(max_length=100,help_text="Required.")

    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('firstname','lastname', 'email','pays','region','ville','rue','zipcode')