"""crud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
""" 
from django.urls import re_path, path
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [  
    path('', views.CalendarView.as_view(), name='adminCalendar'),
    re_path(r'^adminCalendar', views.CalendarView.as_view(), name='adminCalendar'),
    re_path(r'^userCalendar$', views.CalendarViewEmp.as_view(), name='userCalendar'),
    re_path(r'^event/new$', views.event, name='event_new'),
    re_path(r'^event/delete/(?P<event_id>\d+)/$', views.delete_event, name='event_delete'),
    re_path(r'^event/edit/(?P<event_id>\d+)/$', views.event, name='event_edit'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)