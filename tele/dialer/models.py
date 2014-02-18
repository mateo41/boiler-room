from django.forms import ModelForm 
from django.db import models 
# Create your models here.

class Call(models.Model): 
    phone_number = models.CharField(max_length=20)
    call_date = models.DateTimeField('date the call was made')

class CallForm(ModelForm):
    class Meta:
        model = Call
        exclude = ['call_date']
