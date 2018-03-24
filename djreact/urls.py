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
    url(r'^view2/',
        generic.TemplateView.as_view(template_name='view2.html')),
    url(r'^$',
        generic.TemplateView.as_view(template_name='view1.html')),
    url(r'^details',
     views.submit_request, name= 'student_details'),
    url(r'^options',
     views.options, name= 'student_details'),
    url(r'^data/(?P<company>[A-Za-z-]*)$',
     views.parse_csv, name= 'parse'),
    url(r'^(?P<pk>[0-9]+)$', views.DetailsView.as_view(), name='details'),

    url(r'check$', views.index, name='sd'),
    url(r'get_servers$', views.get_servers, name='get_servers'),
    # url(r'check/(?P<company>[A-Za-z_-]*)$', views.get_data, name='getdata'),
    url(r'check/(?P<company>[A-Za-z_-]*)$', views.get_data, name='getdata'),
     url(r'check/(?P<company>[A-Za-z_-]*)/(?P<metric>[A-Za-z_]*)$', views.get_data, name='getdata'),
     url(r'check/(?P<company>[A-Za-z_-]*)/(?P<metric>[A-Za-z_]*)/(?P<server>[a-z\-0-9]*)$', views.get_data, name='getdata'),
    # url(r'data/(?P<company>[a-bA-Z]*>)$', views.index, name='sd'),

    

]
