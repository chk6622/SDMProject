#_*_coding:utf-8_*_
from django.db import models
from django.db.models.fields.related import ForeignKey
from django.contrib import admin
from django.forms import ModelForm
from django import forms
from django.forms.widgets import Widget

# Create your models here.


class BaseModel(models.Model):
    create_time=models.DateTimeField(u'Create time',auto_now_add=True)
    create_user=models.CharField(u'Create user',max_length=200,null=True,blank=True)
    update_time=models.DateTimeField(u'Update time',auto_now=True,null=True,blank=True)
    update_user=models.CharField(u'Update user',max_length=200,null=True,blank=True)
    
    class Meta:
        abstract=True
    
