#!/usr/bin/env python
#coding: utf-8
'''
Created on Sep 10, 2018

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
import logging

logger = logging.getLogger(__name__)


def happyTaskCrontab():
    '''
    user submit happy level task crontab
    create task batch and state at certain time every day
    '''
    try:
        with transaction.atomic():
            TaskState.objects.filter(task_state='1').update(task_state='3')  #update all records which are undone into timeout
            tb=TaskBatch()
            tb.save()
            for user in User.objects.filter(is_active='1', project_id__isnull = False):  #get all users who is active and belong to a project
                ts=TaskState()
                ts.task_batch=tb
                ts.task_state=taskState_choice[0][0]
                ts.user=user
                ts.email=user.email
                ts.slack_account=user.slack_account
                ts.project=user.project
                ts.save()
    except Exception, err:
        logger.error(err)
        
if __name__=='__main__':
    happyTaskCrontab()