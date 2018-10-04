#!/usr/bin/env python
#coding: utf-8
'''
Created on Oct 4, 2018

@author: xingtong
'''
import os
import django
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# import SDMProject.settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SDMProject.settings")
django.setup()

from HappyManagement.models import TaskBatch,TaskState,taskState_choice
# from django.contrib.auth.models import User
from UserManagement.models import CustomUser as User
from django.db import transaction
from slackclient import SlackClient
import logging

logger = logging.getLogger(__name__)


class SlackRobot(object):
    
    def __init__(self):
        self.BOT_ID = 'UD6NR8D28'
        SLACK_BOT_TOKEN='xoxb-417145055956-448773285076-BxLeF7ydbEmFbFzQ1u5yCguS'
        self.slack_client = SlackClient(SLACK_BOT_TOKEN)
        
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
        
    def sendMessageToSlack(self,users=None,userName=None,message=None):
        if users and userName and message:
            userId=users.get(userName)
            if userId:
                self.slack_client.api_call("chat.postMessage", channel=userId, text=message, as_user=True, timeout=1)
    
    
    def createMessage(self):
        host=
        port=8000 
                
    def happinessNotify(self):
        taskStates=TaskState.objects.filter(task_state='1')  #get all people who does not submit happy level
        users=self.getUserInformation()  #get the latest users' information before sending message
        for taskState in taskStates:
            userName=taskState.slack_account
            taskId=taskState.id
            firstName=taskState.user.first_name
            message=r'hello %s, it is time to submit your happy level. Please click following link to submit your happiness. http://127.0.0.1:8000/HappyManagement/addHappyLevel/?task_id=%s' % (firstName,taskId)
            self.sendMessageToSlack(users, userName, message)
        

if __name__=='__main__':
    slackRobot=SlackRobot()
    slackRobot.happinessNotify()
    
    
    
    
    
    
    
    
    
    
    
    
    