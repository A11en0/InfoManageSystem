from django.conf.urls import include, url
from clsMan import views as cls

app_name = "class"
urlpatterns = [
    url(r'main', cls.main, name='class'),
    url(r'^detail$', cls.classDetail),

    url(r'^data$', cls.getData),
    url(r'edit', cls.editCls),

    url(r'delClsInfo', cls.delCls),
    url(r'addClsInfo', cls.addCls),
    url(r'fillSelect', cls.fillSelect),

    url(r'getdetail', cls.getDetailData),
    url(r'delStudInfo', cls.delStud),
    url(r'addStudInfo', cls.addStud),
]