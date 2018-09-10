# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SDMProject.settings")
django.setup()
from django.test import TestCase
from HappyManagement.models import TaskBatch,TaskState,taskState_choice

import sys
import os

from Sys.models import Project
from django.contrib.auth.models import User
from django.db.models import Q
from django.db import transaction


def test():
    try:
        with transaction.atomic():
            TaskState.objects.filter(task_state='1').update(task_state='3')  #update all records which are undone into timeout
            tb=TaskBatch()
            tb.save()
            for user in User.objects.filter(is_active='1', project_id__isnull = False):  #get all users 
                ts=TaskState()
                ts.task_batch=tb
                ts.task_state=taskState_choice[0][0]
                ts.user=user
                ts.email=user.email
                ts.project=user.project
                ts.save()
    except Exception, err:
        print err

if __name__=='__main__':
    test()
    
