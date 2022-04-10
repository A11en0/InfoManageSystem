from django.conf.urls import include, url
from studscore import views as score

app_name = 'studscore'
urlpatterns = [
    url(r'main', score.main, name='studscore'),
    url(r'data', score.getData),

    url(r'edit', score.editScore),

    url(r'delScoreInfo', score.delScore),
    url(r'addScoreInfo', score.addScore),
    url(r'fillSelect', score.fillSelect),
    url(r'fillNum', score.fillNum),
    url(r'fillClass', score.fillClass)
]