"""djreact URL Configuration

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
from watch import views

from django.conf.urls import url
from django.contrib import admin
from django.views import generic

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^data/(?P<company>[A-Za-z-]*)$',views.parse_csv, name= 'parse'),

    url(r'$', views.index, name='sd'),

    # url(r'check/(?P<company>[A-Za-z_-]*)$', views.get_data, name='getdata'),
    url(r'(?P<company>[A-Za-z_-]*)$', views.get_data, name='getdata'),
     url(r'(?P<company>[A-Za-z_-]*)/(?P<metric>[A-Za-z_]*)$', views.get_data, name='getdata'),
     url(r'(?P<company>[A-Za-z_-]*)/(?P<metric>[A-Za-z_]*)/(?P<server>[A-Za-z\-0-9]*)$', views.get_data, name='getdata'),
    # url(r'data/(?P<company>[a-bA-Z]*>)$', views.index, name='sd'),

    

]
