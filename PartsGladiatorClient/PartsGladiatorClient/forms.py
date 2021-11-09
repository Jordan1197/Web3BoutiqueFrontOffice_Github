from django import forms
from PartsGladiatorClient.Models import *

class ContactForm(forms.Form):
    name = forms.CharField(label='Name',widget=forms.TextInput(attrs={'placeholder':'Votre Nom'}), max_length=50)
    mail = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Votre mail'}),max_length=200)
    subject = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Sujet'}),max_length=500)
    message = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Message'}),max_length=500)
    

class SearchForm(forms.Form):
    brand = forms.CharField(label='Marque', widget=forms.TextInput(attrs={'placeholder':'Votre Nom'}), max_length=50)
    characteristic = forms.CharField(label='Caractéristique', widget=forms.TextInput(attrs={'placeholder':'Votre Nom'}), max_length=50)
    promotion = forms.CharField(label='Promotion', widget=forms.TextInput(attrs={'placeholder':'Votre Nom'}), max_length=50)
    category = forms.ChoiceField(choices=CHOICES ,label='Catégorie', widget=forms.RadioSelect)