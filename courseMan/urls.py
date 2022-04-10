from django.conf.urls import include, url
from courseMan.views import *

app_name = "course"
urlpatterns = [

    url(r'main', main, name='course'),
    url(r'data', getData),
    
    url(r'edit', editCourse),

    url(r'delCourseInfo', delCourse),
    url(r'addCourseInfo', addCourse),
    url(r'select_class$', select_class),
    url(r'select_teacher$', select_teacher)
]