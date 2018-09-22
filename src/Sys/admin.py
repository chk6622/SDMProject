#!/usr/bin/env python
# coding: utf-8
'''
Created on Sep 2, 2018

@author: xingtong
'''
from django.contrib import admin
from models import Project
from django.contrib.auth.models import Permission

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    list_display = (('projectName','projectDescribe','is_active')) # list
    search_fields = (('projectName','is_active'))

admin.site.register(Project,ProjectAdmin)
admin.site.register(Permission)

admin.site.site_header = 'Team Happiness Research System'
