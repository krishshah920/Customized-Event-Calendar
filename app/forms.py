from django import forms  
from .models import *
from django.forms import ModelForm, DateInput

class DateInput(forms.DateInput):
    input_type = 'date'
         
          
choice = [('True','Admin Only   '),('False', 'Both')]
class EventForm(ModelForm):
  
  class Meta:

    model = Event
    # datetime-local is a HTML5 input type, format to make date time show on fields
    widgets = {
      'date': DateInput(format='%Y-%m-%d'),
      'visibility' : forms.RadioSelect(choices=choice)
    }
    fields = '__all__'    