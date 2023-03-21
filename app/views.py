from django.shortcuts import render, redirect ,HttpResponse ,  HttpResponseRedirect, get_object_or_404
from django.contrib import messages
from .models import *
from .forms import *

# from .models import Addemployee, Leave_App, Event, Admin_Login
# from .forms import AddemployeeForm, Admin_LoginForm, EventForm, Leave_AppForm 
from django.conf import settings
from django.core.mail import send_mail 
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from datetime import datetime
from datetime import date
import os 
from django.db import connection
from django.db.models import Count 
from django.urls import reverse
from .utils import Calendar, Eventcal
import calendar
from django.utils.safestring import mark_safe
from datetime import datetime, timedelta
from django.views import generic
 
class CalendarView(generic.ListView):
    
    model = Event
    template_name = 'adminCalendar.html'
     
    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)

        # use today's date for the calendar
        today = str(get_date(self.request.GET.get('day', None)))
        today_year, today_month, today_date = (int(x) for x in today.split('-')) 
        adminStatus = True
        d = get_date(self.request.GET.get('month', None))
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        cal = Calendar(d.year, d.month, today_date, today_month, today_year, adminStatus)
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        event = Eventcal(d.year, d.month, adminStatus)
        html_event = event.formatmonth(withyear=True)
        context['event'] = mark_safe(html_event)
         
        return context
    
class CalendarViewEmp(generic.ListView):
    
    model = Event
    template_name = 'userCalendar.html'
    
     
    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)

        # use today's date for the calendar
        today = str(get_date(self.request.GET.get('day', None))) 
        today_year, today_month, today_date = (int(x) for x in today.split('-')) 
        
        d = get_date(self.request.GET.get('month', None))
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        adminStatus = False
        cal = Calendar(d.year, d.month, today_date, today_month, today_year, adminStatus)
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        event = Eventcal(d.year, d.month, adminStatus)
        html_event = event.formatmonth(withyear=True)
        context['event'] = mark_safe(html_event) 
        return context
    

def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month

def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month

def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return date.today()


# Event add
def event(request, event_id=None):
    instance = Event()
    if event_id:
        instance = get_object_or_404(Event, pk=event_id)
    else:
        instance = Event()
    
    form = EventForm(request.POST or None, instance=instance)
    if request.POST and form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('adminCalendar'))
    return render(request, 'event.html', {'form': form})

def delete_event(request, event_id):
    instance = Event()
    if event_id:
        instance = get_object_or_404(Event, pk=event_id)
    else:
        instance = Event()
    instance.delete()
    return redirect('adminCalendar')


 