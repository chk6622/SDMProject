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
from ProjectManagement.models import Project
# from django.contrib.auth.models import User
from UserManagement.models import CustomUser as User
from numpy.ma.testutils import __all__masked
import uuid


# Create your models here.
happyLevel_choice=[
                    ('1',u'Exited'),
                    ('2',u'Happy'),
                    ('3',u'Normal'),
                    ('4',u'Unhappy'),
                    ('5',u'Angry')
                    ]

taskState_choice=[
    ('1','Undone'),
    ('2','Done'),
    ('3','Timeout')
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
        projects=Project.objects.all()
        for project in projects:
            lReturn.append({project.id,project.projectName})
    except Exception, err:
        pass
    return lReturn

class TaskBatch(models.Model):
    '''
    Task batch class
    '''
    create_time=models.DateTimeField(u'Task batch create time',auto_now_add=True)
    def __unicode__(self):
        return 'Task batch %s' % self.create_time
    
class TaskState(models.Model):
    '''
    Task state class
    '''
    id= models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    task_batch=models.ForeignKey(TaskBatch,null=True,blank=True)
    user=models.ForeignKey(User,null=True,blank=True)
    email=models.CharField(u'Email',max_length=100,null=True,blank=True)
    slack_account=models.CharField(u'Slack account',max_length=100,null=True,blank=True)
    project=models.ForeignKey(Project,null=True,blank=True)
    task_state=models.CharField(u'Task state level',max_length=50,choices=taskState_choice,null=True,blank=True)
    next_notify_time=models.DateTimeField(u'Next notify time',null=True,blank=True)
    notify_count=models.BigIntegerField(u'Notify Count', default=0)
    
    class Meta:
        ordering=[]
        permissions=(
                    ('query_taskstate',u'can query task state'),
                    ('export_taskstate',u'can export task state'),
                     )

class TaskStateForm(forms.ModelForm):
    email_qry=forms.CharField(label=u'Email',max_length=50, required=False)
    task_state_qry=forms.ChoiceField(label=u'Task state',help_text=u'',required=False,choices=getChoice(taskState_choice,True),widget=forms.Select)
    project_qry=forms.ModelChoiceField(label=u'Project',queryset=Project.objects.all(),required=False)
    b_create_time=forms.DateField(label=u'Create time',help_text=u' yyyy-MM-dd',required=False,input_formats=(settings.GLOBAL_DATE_FORMAT,),widget=widgets.DateInput(format=settings.GLOBAL_DATE_FORMAT,attrs={'size':'25'}))
    e_create_time=forms.DateField(label=u'To create time',help_text=u' yyyy-MM-dd',required=False,input_formats=(settings.GLOBAL_DATE_FORMAT,),widget=widgets.DateInput(format=settings.GLOBAL_DATE_FORMAT,attrs={'size':'25'}))
    class Meta:
        model=TaskState
        fields='__all__'
        initial={}


class HappyLevel(BaseModels.BaseModel):    
    personal_happy_level=models.CharField(u'Personal happy level',max_length=50,choices=happyLevel_choice,null=True,blank=False)
    project_happy_level=models.CharField(u'Project happy level',max_length=50,choices=happyLevel_choice,null=True,blank=False)
    project=models.ForeignKey(Project,null=True,blank=True)
    create_user=models.ForeignKey(User,null=True,blank=True)
    # update_user should be User Foreign Key, but I have to set related_name, because I already have one User FK in model
    update_user=models.ForeignKey(User,null=True,blank=True, related_name='happylevel_updateuser')
    
    def __unicode__(self):
        return ''.join((self.create_time,self.create_user,self.personal_happy_level,self.project_happy_level))
    
    class Meta:
        ordering=['-create_time']
        permissions=(
                    ('query_happylevel',u'can query happy level'),
                    ('export_happylevel',u'can export happy level'),
                     )
        
    def getFormatObj(self):
        rList=[]
        attrNames=('project_id','create_time','personal_happy_level','project_happy_level')
        attrlabels=('Project','Create time','Personal happy level','Project happy level')
        for attr in attrNames:                
            tmpAttr=self.__dict__.get(attr)
            if tmpAttr:
                if isinstance(tmpAttr,datetime.datetime):
                    tmpAttr=tmpAttr.strftime(settings.GLOBAL_DATE_FORMAT)
                    rList.append(tmpAttr)
                elif attr=='project_happy_level':
                    happy_name=''
                    for (value,name) in happyLevel_choice:
                        if value==tmpAttr:
                            happy_name=name
                            break
                    rList.append(happy_name)
                elif attr=='personal_happy_level':
                    happy_name=''
                    for (value,name) in happyLevel_choice:
                        if value==tmpAttr:
                            happy_name=name
                            break
                    rList.append(happy_name)
                elif attr=='project_id':
                    rList.append(self.project.projectName)
                else:
                    rList.append(tmpAttr)
            else:
                rList.append('')
        return attrlabels,rList
        
class HappyLevelForm(forms.ModelForm):
    id=forms.CharField(label=u'Id', required=False,widget=forms.HiddenInput)
    b_create_time=forms.DateField(label=u'Create time',help_text=u' yyyy-MM-dd',required=False,input_formats=(settings.GLOBAL_DATE_FORMAT,),widget=widgets.DateInput(format=settings.GLOBAL_DATE_FORMAT,attrs={'size':'25'}))
    e_create_time=forms.DateField(label=u'To create time',help_text=u' yyyy-MM-dd',required=False)
    
    create_user_qry=forms.CharField(label=u'Create user',help_text=u'',required=False)
    project_qry=forms.ChoiceField(label=u'Project',help_text=u'',required=False,choices=[],widget=forms.Select)
    
    personal_happy_level_qry=forms.ChoiceField(label=u'Personal happy level',help_text=u'',required=False,choices=getChoice(happyLevel_choice,True),widget=forms.Select)
    project_happy_level_qry=forms.ChoiceField(label=u'Project happy level',help_text=u'',required=False,choices=getChoice(happyLevel_choice,True),widget=forms.Select)
    
    personal_happy_level=forms.ChoiceField(label=u'Personal happy level',help_text=u'',required=True,choices=getChoice(happyLevel_choice,True),widget=forms.RadioSelect)
    project_happy_level=forms.ChoiceField(label=u'Project happy level',help_text=u'',required=True,choices=getChoice(happyLevel_choice,True),widget=forms.RadioSelect)
    
    
    class Meta:
        model=HappyLevel
        fields='__all__' #('id','b_create_time','e_create_time','create_user_qry','project_qry','personal_happy_level_qry','project_happy_level_qry','personal_happy_level','project_happy_level','create_user','project')     
        initial={}
        
    def __init__(self,*args,**kwargs):
        super(HappyLevelForm,self).__init__(*args,**kwargs)
        projects=getAllProject()
        self.fields['project_qry'].choices=getChoice(projects,hasBlank=True)
        self.fields['project'].choices=getChoice(projects,hasBlank=True)
        

    