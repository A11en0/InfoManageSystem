from django.conf.urls import include, url
from stdMan import views as std

app_name = 'student'
urlpatterns = [

    url(r'main', std.main, name='student'),
    url(r'data', std.getData),
    
    url(r'edit', std.editStud),
    
    url(r'delStudInfo', std.delStud),
    url(r'addStudInfo', std.addStud),
    url(r'fillSelect', std.fillSelect)
]