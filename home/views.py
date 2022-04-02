
from pyexpat.errors import messages
from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import contact
def index(request):
    return render(request, 'index.html')
def Contact(request):
    if request.method =="POST":
        email = request.POST.get('email')
        pass2 = request.POST.get('pass2')
        Contact = contact(email=email,pass2=pass2)
        Contact.save()
    return render(request,'Contact.html')


 
def home(request):
    return render(request,'index.html')

