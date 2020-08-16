from django.urls import path
from django.shortcuts import HttpResponse
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns =[
    path('',  login_required(views.index), name='OutletHome'),
    path('about/',  login_required(views.about), name='AboutUs'),
    path('contact/',  login_required(views.contact), name='Contact'),
    path('productview/<int:id>',  login_required(views.prodview), name='ProductView'),
]
