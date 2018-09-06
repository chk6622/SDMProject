#!/usr/bin/env python
# coding: utf-8
"""ResearchMethodProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import include,url
from django.contrib import admin
from Sys import url as SysUrl
from UserManagement import url as userUrl
from django.contrib.auth.views import login,logout,password_change,password_change_done
from Sys.SysView import loginSuccess,changePasswordDone
from django.conf.urls.static import static
import SDMProject.views as HtmlViews 
import settings
import django.views.static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^Sys/',include(SysUrl)),
    url(r'^UserManagement/',include(userUrl)),
    
    url(r'media/(?P<path>.*)$',django.views.static.serve,{'document_root':settings.MEDIA_ROOT},name='media'),  #upload file
    url(r'static/(?P<path>.*)$',django.views.static.serve,{'document_root':settings.STATIC_ROOT},name='static'),  #static web page
#     url(r'html/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.TEMPLATES[0].get('DIRS')[0]},name='html'),  #static web page
    url(r'^html/center.html',HtmlViews.center),
    url(r'^html/down.html',HtmlViews.down),
    url(r'^html/left.html',HtmlViews.left),
    url(r'^html/middel.html',HtmlViews.middel),
    url(r'^html/right.html',HtmlViews.right),
    url(r'^html/welcome.html',HtmlViews.welcome),
    url(r'^html/top.html',HtmlViews.top),
    
    
    url(r'^accounts/profile/$',loginSuccess),  #login success forward page
    url(r'^logout/',logout,{'next_page':'/'}),  #next_page：logout success forward page
    url(r'^$', login,{'template_name':'login.html'}),   #template_name:login page
]
