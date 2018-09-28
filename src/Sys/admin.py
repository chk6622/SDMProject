#!/usr/bin/env python
# coding: utf-8
'''
Created on Sep 2, 2018

@author: xingtong
'''
from django.contrib import admin
from django.contrib.auth.models import Permission


# Register your models here.

admin.site.register(Permission)

admin.site.site_header = 'Team Happiness Research System'