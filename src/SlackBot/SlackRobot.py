#!/usr/bin/env python
#coding: utf-8
'''
Created on Oct 4, 2018

@author: xingtong
'''
import os
import django
import sys
from Common.CommonTools import get_host_ip
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# import SDMProject.settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SDMProject.settings")
django.setup()

from HappyManagement.models import TaskBatch,TaskState,taskState_choice
# from django.contrib.auth.models import User
from UserManagement.models import CustomUser as User
from django.db import transaction
from slackclient import SlackClient
from Common.CommonTools import *
import logging
from django.utils import timezone
import time

logger = logging.getLogger(__name__)


class SlackRobot(object):
    
    def __init__(self):
        self.BOT_ID = 'UD6NR8D28'
        SLACK_BOT_TOKEN='xoxb-417145055956-448773285076-BxLeF7ydbEmFbFzQ1u5yCguS'
        self.slack_client = SlackClient(SLACK_BOT_TOKEN)
        self.host=r'104.210.70.125'  #get_host_ip()
        self.port=80
        
    def getSlackAccountInformation(self):
        '''
        get all users information
        @return: a map, it's key is username and value is user id 
        '''
        users={}
        memberList = self.slack_client.api_call("users.list").get('members')
        for member in memberList:
            users.update({member.get('name'):member.get('id')})
        return users
        
    def sendMessageToSlack(self,users=None,slackAccount=None,message=None,attachment=None):
        if users and slackAccount and message:
            slackId=users.get(slackAccount)
            if slackId:
                self.slack_client.api_call("chat.postMessage", channel=slackId, text=message, attachments=attachment, as_user=True, timeout=3)
#                 self.slack_client.api_call("chat.postMessage", channel=userId, text=message, as_user=True, timeout=1)
    
    
    def createSubmitUrl(self,taskId=''):
        uReturn=r'http://%s/HappyManagement/addHappyLevel/?task_id=%s' % (self.host,taskId)
#         message=r'Hi guys, would your like to submit your happiness now?'
        return uReturn
    
    def createAttachment(self, submitUrl=None, value= None, userName= None):
        attachment=[{ 
        "title": "Hi %s, would your like to submit your happiness now?" % userName, 
        'title_link': submitUrl,
        "text": "You can click the green button to submit your happiness, or you can click red buttons to postpone your submitting time.", 
        'callback_id':'delay_submit',
        "actions": [ 
            { 
             "name": "Happiness_submit", 
             "text": "Submit", 
             "type": "button", 
             "url": submitUrl,
             'style' : 'primary'
            },
            { 
             "name": "Postpone_5_m", 
             "text": "5 minutes", 
             "type": "button", 
             'style' : 'danger',
             "value": '%s;5' % value,
            },
            { 
             "name": "Postpone_10_m", 
             "text": "10 minutes", 
             "type": "button", 
             'style' : 'danger',
             "value": '%s;10' % value,
            },
            { 
             "name": "Postpone_20_m", 
             "text": "20 minutes", 
             "type": "button", 
             'style' : 'danger',
             "value": '%s;20' % value,
            }
            ] 
        
        }] 
#         print attachment
        return attachment
                
    def happinessNotify(self):
        taskStates=TaskState.objects.filter(task_state='1')  #get all people who does not submit happy level
        users=self.getSlackAccountInformation()  #get the latest slack account information before sending message
        total_notify_number=0
        for taskState in taskStates:
            slackAccount=taskState.slack_account
            taskId=taskState.id
#             print taskId
#             firstName=taskState.user.first_name
            message=' ' #self.createMessage(firstName, taskId)
            url=self.createSubmitUrl(taskId)
#             print url
            attachment=self.createAttachment(submitUrl=url,value='%s' % taskId, userName=taskState.user.first_name)
            
            notifyCount=taskState.notify_count
            waitTime=2 #get_postpone_time(notifyCount)
            notifyTime = taskState.next_notify_time
            now = timezone.now()
            if not notifyTime:
                notifyTime = now
            if notifyTime <= now:
                self.sendMessageToSlack(users=users, slackAccount=slackAccount, message=message, attachment=attachment)  #notify
                total_notify_number += 1
                nextNotifyTime = calcute_datetime(now, waitTime)
                taskState.notify_count = notifyCount + 1
                taskState.next_notify_time = nextNotifyTime
                taskState.save()
        print 'Total notify number is %d' % total_notify_number
            
#     def exectue(self):
#         slackRobot=SlackRobot()
#         while True:
#             slackRobot.happinessNotify()
#             time.sleep(10)
        

if __name__=='__main__':
#     taskId='2d829ba9-36be-4d9f-9236-e591dee49c15'
#     taskStates=TaskState.objects.filter(id='%s' % taskId)
#     print taskStates[0].id
#     taskState=TaskState.objects.get(id='%s' % taskId)
#     print taskState.id
    slackRobot=SlackRobot()
    slackRobot.happinessNotify()
    
    
    
    
    
    
    
    
    
    
    
    
    