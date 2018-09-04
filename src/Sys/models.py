#!/usr/bin/env python
# coding: utf-8
'''
Created on Sep 2, 2018

@author: xingtong
'''
from django import forms
from django import forms
from django.contrib import admin
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin,GroupAdmin
from django.contrib.auth.forms import *
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.db import models
from django.db.models.fields.related import ForeignKey
from django.forms import ModelForm
from django.forms.widgets import Widget

# Create your models here.

class Project(models.Model):
    projectName = models.CharField(max_length=30)
    projectDescribe=models.TextField()
    is_active = models.BooleanField(
        default=True,
        help_text=(
            'Designates whether this project should be treated as active. '
        ),
    )
    
    def __str__(self):
        return self.projectName


class MyProfileForm(UserChangeForm):
    project = forms.ModelChoiceField(queryset=Project.objects.filter(('is_active','1')),)
#     def __init__(self, *args, **kwargs):
#         super(MyProfileForm, self).__init__(*args, **kwargs)
#         self.fields.get('groups').label = 'Roles'
#         self.fields.get('groups').help_text = 'The roles this user belongs to. A user will get all permissions granted to each of their roles. Hold down "Control", or "Command" on a Mac, to select more than one.'
        

class ProfileBase(type):
 
    def __new__(cls, name, bases, attrs):
        module = attrs.pop('__module__')
        parents = [b for b in bases if isinstance(b, ProfileBase)]
        if parents:
            fields = []
            for (obj_name, obj) in attrs.items():
                if isinstance(obj, models.Field):
                    fields.append(obj_name)
                User.add_to_class(obj_name, obj)
            formList = list(UserAdmin.fieldsets)
            formList.append((name, {'fields':fields}))
            UserAdmin.fieldsets = formList
            UserAdmin.form = MyProfileForm
        return super(ProfileBase, cls).__new__(cls, name, bases, attrs)
 
 
class Profile(object):
    __metaclass__ = ProfileBase
 
     
class MyProfile(Profile):
    project = models.ForeignKey(Project)
    

