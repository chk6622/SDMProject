#!/usr/bin/env python
#coding: utf-8
'''
Created on Oct 6, 2018

@author: xingtong
'''

import os
import django
import sys
# from Common.CommonTools import get_host_ip
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
from SlackBot import SlackRobot


        
if __name__=='__main__':
    slackRobot=SlackRobot.SlackRobot()
    slackRobot.happinessNotify()