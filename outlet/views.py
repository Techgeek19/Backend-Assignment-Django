from django.shortcuts import render, HttpResponse
from django.contrib import messages
from .models import Product, Contact
from math import ceil
import json

# Create your views here.

def index(request):
    allprod= Product.objects.all()
    return render(request,'outlet/index.html',{'allprod':allprod})

def about(request):
    return render(request,'outlet/about.html')

def contact(request):
    if request.method=="POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        message = request.POST.get('message', '')
        contact = Contact(name=name, email=email, message=message)
        contact.save()
        messages.info(request, 'Thanks for connecting with us. Your message has been successfully delivered')
    return render(request,'outlet/contact.html', {})


def prodview(request, id):
    #fetching product using id
    obj= Product.objects.filter(id=id)
    print(obj[0])
    return render(request,'outlet/prodview.html', {'obj':obj[0]})


    
