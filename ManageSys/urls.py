"""ManageSys URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""

from django.conf.urls import include, url, handler404, handler500
from django.contrib import admin
from login import views as login
from examMan.views import main

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', main),
    url(r'^scorequery/', include('scorequery.urls')),
    url(r'^teacher/', include('teacherMan.urls')),
    url(r'^class/', include('clsMan.urls')),
    url(r'^student/', include('stdMan.urls')),
    url(r'^course/', include('courseMan.urls')),
    url(r'^studscore/', include('studscore.urls')),
    url(r'^exam/', include('examMan.urls')),
    url(r'^login/', login.do_login, name='login'),
    url(r'^logout/', login.do_logout, name='logout'),
    url(r'^register/$', login.do_register, name='register'),
    url(r'^register_success/$', login.register_success, name='register_success'),
]


