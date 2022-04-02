from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index , name = 'index' ),
    path('Contact', views.Contact , name = 'Contact' ),
    path('home', views.home , name = 'home' )
]