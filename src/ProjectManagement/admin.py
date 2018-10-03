# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Project

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    list_display = (('projectName','projectDescribe','is_active')) # list
    search_fields = (('projectName','is_active'))



admin.site.register(Project,ProjectAdmin)