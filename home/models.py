import email
from unittest.util import _MAX_LENGTH
from django.db import models
from django.forms import CharField, PasswordInput

class contact(models.Model):
   email = models.CharField(max_length=50)
   pass2 = models.CharField(max_length=30)

   def __str__(self):
       return self.email
   
   
   
