# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.db import models
from Common import BaseModels
import datetime
from SDMProject import settings
from django import forms
from django.forms import widgets
from django.forms.widgets import Widget
from Sys.models import Project


# Create your models here.
happyLevel_choice=[
                    ('1',u'no happy'),
                    ('2',u'normal'),
                    ('3',u'happy')
                    ]

def getChoice(choiceList,hasBlank=False):
    returnList=[]
    if choiceList and isinstance(choiceList,list):
        if hasBlank:
            returnList.append((u'',u'-'*25))
            returnList.extend(choiceList)
        else:
            returnList.extend(choiceList)
    return returnList

def getAllProject():
    lReturn=[]
    try:
        lReturn=Project.objects.filter({'is_active':'1'})
    except Exception, err:
        pass
    return lReturn

class HappyLevel(BaseModels.BaseModel):
    
    personal_happy_level=models.CharField(u'personal happy level',max_length=50,choices=happyLevel_choice,null=True,blank=True)
    project_happy_level=models.CharField(u'project happy level',max_length=50,choices=happyLevel_choice,null=True,blank=True)
    project=models.ForeignKey(Project)
    
    def __unicode__(self):
        return ''.join((self.createTime,self.createUser,self.personal_happy_level,self.project_happy_level))
    
    class Meta:
        ordering=['-create_time']
        permissions=(
                     ('export_happylevel',u'can export happy level'),
                     )
        
class HappyLevelForm(forms.ModelForm):
    id=forms.CharField(label=u'id', required=False,widget=forms.HiddenInput)
    b_create_time=forms.DateField(label=u'from create time',help_text=u' yyyy-MM-dd',required=False)
    e_create_time=forms.DateField(label=u'to create time',help_text=u' yyyy-MM-dd',required=False)
    
    create_user_qry=forms.CharField(label=u'create user',help_text=u'',required=False)
    project_qry=forms.ChoiceField(label=u'project',help_text=u'',required=False,choices=[],widget=forms.Select)
    
    personal_happy_level_qry=forms.ChoiceField(label=u'personal happy level',help_text=u'',required=False,choices=getChoice(happyLevel_choice,True),widget=forms.Select)
    project_happy_level_qry=forms.ChoiceField(label=u'project happy level',help_text=u'',required=False,choices=getChoice(happyLevel_choice,True),widget=forms.Select)
    
    
    class Meta:
        model=HappyLevel
        fields=('id','b_create_time','e_create_time','create_user_qry','project_qry','personal_happy_level_qry','project_happy_level_qry')     
        initial={}
        
    def __init__(self,*args,**kwargs):
        super(HappyLevelForm,self).__init__(*args,**kwargs)
        projects=getChoice(getAllProject())
        self.fields['project_qry'].choices=getChoice(projects,hasBlank=False)
        self.fields['project'].choices=getChoice(projects,hasBlank=True)