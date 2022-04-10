from django.conf.urls import include, url
from teacherMan import views as tech

app_name = 'teacher'
urlpatterns = [
    url(r'main', tech.main, name='teacher'),
    url(r'data', tech.getData),

    url(r'edit', tech.editTech),

    url(r'delTechInfo', tech.delTech),
    url(r'addTechInfo', tech.addTech),
    #url(r'fillSelect', std.fillSelect)

]