#!/usr/bin/env python
# coding: utf-8
'''
Created on Sep 6, 2018

@author: xingtong
'''
import sys

from django.conf.urls import include, url
from django.contrib import admin
from HappyManagement.HappyManagementView import *



urlpatterns = [
 
    url(r'^query/', query), 
    url(r'^add/', addOrEdit), 
    url(r'^edit/', addOrEdit),
    url(r'^saveOrUpdate/', saveOrUpdate), 

]
