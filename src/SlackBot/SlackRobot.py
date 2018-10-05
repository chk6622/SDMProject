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

logger = logging.getLogger(__name__)


class SlackRobot(object):
    
    def __init__(self):
        self.BOT_ID = 'UD6NR8D28'
        SLACK_BOT_TOKEN='xoxb-417145055956-448773285076-BxLeF7ydbEmFbFzQ1u5yCguS'
        self.slack_client = SlackClient(SLACK_BOT_TOKEN)
        self.host=get_host_ip()
        self.port=8000 
        
    def getUserInformation(self):
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
                self.slack_client.api_call("chat.postMessage", channel=slackId, text=message, attachments=attachment, as_user=True, timeout=1)
#                 self.slack_client.api_call("chat.postMessage", channel=userId, text=message, as_user=True, timeout=1)
    
    
    def createMessage(self,userName='',taskId=''):
#         message=r'Hello %s, it is time to submit your happy level. Please click following link to submit your happiness. http://%s:8000/HappyManagement/addHappyLevel/?task_id=%s' % (userName,self.host,taskId)
        message=r'Hi guys, would your like to submit your happiness now?'
        return message
    
    def createAttachment(self):
        attachment=[{ 
        "title": "Hi guys, would your like to submit your happiness now?", 
        'title_link': 'http://127.0.0.1:8000/',
        "text": "Choose a button to click", 
        'callback_id':'delay_submit',
        "actions": [ 
            { 
             "name": "buttonName", 
             "text": "Submit happiness now!", 
             "type": "button", 
             "url": 'http://localhost:8000/',
             'style' : 'primary'
            },
            { 
             "name": "delay_submit", 
             "text": "Delay submit!", 
             "type": "button", 
             'style' : 'danger',
             "value": 'delay_submit',
             
            }
            ] 
        
        }] 
        return attachment
                
    def happinessNotify(self):
        taskStates=TaskState.objects.filter(task_state='1')  #get all people who does not submit happy level
        users=self.getUserInformation()  #get the latest users' information before sending message
        for taskState in taskStates:
            slackAccount=taskState.slack_account
            taskId=taskState.id
            firstName=taskState.user.first_name
            message=' ' #self.createMessage(firstName, taskId)
            attachment=self.createAttachment()
            self.sendMessageToSlack(users=users, slackAccount=slackAccount, message=message, attachment=attachment)
        

if __name__=='__main__':
    slackRobot=SlackRobot()
    slackRobot.happinessNotify()
    
    
    
    
    
    
    
    
    
    
    
    
    