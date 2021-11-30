from django import forms
from PartsGladiatorClient.Models import *


    

class SearchForm(forms.Form):
    brand = forms.CharField(label='Name', widget=forms.TextInput(attrs={'placeholder':'Votre Nom'}), max_length=50)

