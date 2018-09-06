# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django import forms
from django.forms import widgets
from django.forms.widgets import Widget
from SDMProject import settings
from django.contrib.auth.models import User

# Create your models here.
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
        model=User
        fields=('id','first_name','last_name','email','nationality','hobby')     
        initial={}