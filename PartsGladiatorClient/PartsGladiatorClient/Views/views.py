from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import HttpResponseRedirect
from Prototype.forms import *

def index(request):
    
    return HttpResponse(request)