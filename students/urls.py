"""students URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from students import views

urlpatterns = [
    url(r'^$', views.StudentListView.as_view(), name='list_view'),
    url(r'^(?P<pk>\d+)/', views.StudentDetailView.as_view(), name='detail'),
    url(r'^add/$', views.StudentCreateView.as_view(), name='add'),
    url(r'^edit/(?P<pk>\d+)/$', views.StudentUpdateView.as_view(), name='edit'),
    url(r'^remove/(?P<pk>\d+)/$', views.StudentDeleteView.as_view(), name='remove'),
]
