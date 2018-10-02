#!/usr/bin/env python
# coding: utf-8
'''
Created on Sep 2, 2018

@author: xingtong
'''
# from __future__ import unicode_literals

from django.db import models
from django import forms
from django.forms import widgets
from django.forms.widgets import Widget
from SDMProject import settings
from django.contrib.auth.models import User
from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.db import models
from django.forms import ModelForm
from django.forms.widgets import Widget
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import AbstractUser
from ProjectManagement.models import Project


class CustomUser(AbstractUser):
    # add additional fields in here
    project = models.ForeignKey(Project,null=True,blank=True)
    nationality=models.CharField(u'Nationality',max_length=30,null=True,blank=True)
    hobby=models.CharField(u'hobby',max_length=30,null=True,blank=True)
    is_email = models.BooleanField(u'isEmail',default=False)

    def __str__(self):
        return self.username
    
    class Meta:
        permissions = (
            ("query_customuser", "Can query user"),
        )

class UserManageForm(forms.ModelForm):
    id=forms.CharField(label=u'id', required=False,widget=forms.HiddenInput)
    first_name=forms.CharField(label=u'first_name',max_length=50, required=False)
    first_name_qry=forms.CharField(label=u'first_name',max_length=50, required=False)
    last_name=forms.CharField(label=u'last_name',max_length=50, required=False)
    last_name_qry=forms.CharField(label=u'last_name',max_length=50, required=False)
    email=forms.CharField(label=u'email',max_length=50, required=False)
    email_qry=forms.CharField(label=u'email',max_length=50, required=False)
    nationality=forms.CharField(label=u'nationality',max_length=50, required=False)
    nationality_qry=forms.CharField(label=u'nationality',max_length=50, required=False)
    hobby=forms.CharField(label=u'hobby',max_length=50, required=False)
    hobby_qry=forms.CharField(label=u'hobby',max_length=50, required=False)
    
    class Meta:
        model=CustomUser
        fields=('id','first_name','last_name','email','nationality','hobby')     
        initial={}
        

    

from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class CustomUserCreationForm(UserCreationForm):
#     project = forms.ModelChoiceField(queryset=Project.objects.filter(('is_active','1')),)
#     nationality=forms.CharField(label=u'Nationality',max_length=30,required=False)
#     hobby=forms.CharField(label=u'Hobby',max_length=30,required=False)
#     is_email = forms.BooleanField(label=u'isEmail',required=False)
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields=('project','nationality','hobby','is_email')

class CustomUserChangeForm(UserChangeForm):

    
#     project = forms.ModelChoiceField(queryset=Project.objects.filter(('is_active','1')),)
#     nationality=forms.CharField(label=u'Nationality',max_length=30,required=False)
#     hobby=forms.CharField(label=u'Hobby',max_length=30,required=False)
#     is_email = forms.BooleanField(label=u'isEmail',required=False)
    
    class Meta:
        model = CustomUser
        fields=('project','nationality','hobby','is_email')
 
        
        
        
        
        
        
        
        
        
        
        
        
        
        