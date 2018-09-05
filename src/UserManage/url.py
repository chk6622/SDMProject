#!/usr/bin/env python
# coding: utf-8
'''
Created on Sep 2, 2018

@author: xingtong
'''
import sys

from django.conf.urls import include, url
from django.contrib import admin
from UserManage.UserManageViews import *



urlpatterns = [
 
    url(r'^query/', query), 
    url(r'^add/', addOrEdit), 
    url(r'^edit/', addOrEdit),
    url(r'^saveOrUpdate/', saveOrUpdate), 

]
