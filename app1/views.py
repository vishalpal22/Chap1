from django.shortcuts import render
from django.http import HttpRequest
from django.shortcuts import render
from .forms import *
# Create your views here.
# def home(request):
#     return render(request,'day1.html')

def contact_form(request):
    if request.method == "POST":
        form = App1Form(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = App1Form() 
    
    return render(request,'day1.html')


