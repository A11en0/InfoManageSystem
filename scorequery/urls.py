from django.conf.urls import include, url
from scorequery.views import *
#from courseMan.views import *


app_name = "scorequery"
urlpatterns = [
    url(r'main', main, name='score'),
    url(r'data', getData),
]