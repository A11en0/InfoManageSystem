from django.conf.urls import include, url
from examMan.views import *

app_name = "exam"
urlpatterns = [

    url(r'main', main, name='exam'),
    url(r'data', getData),
    #url(r'initScore', initScore),

    url(r'edit', editScore),

    url(r'delExamInfo', delExam),
    url(r'addExamInfo', addExam),

    url(r'entryScore', entryScore, name="entryscore"),

    url(r'select_class$', select_class),
    url(r'select_type$', select_type),
    url(r'select_course$', select_course)
]