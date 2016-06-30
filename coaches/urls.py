from django.conf.urls import patterns, url

from coaches import views

urlpatterns = [
    url(r'^(?P<coach_id>\d+)/$', views.detail, name='detail'),
]
