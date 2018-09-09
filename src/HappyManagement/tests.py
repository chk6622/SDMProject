# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SDMProject.settings")
django.setup()
import SDMProject.urls
from django.test import TestCase
from HappyManagement.models import TaskBatch,TaskState,taskState_choice

import sys
import os

from Sys.models import Project
from django.contrib.auth.models import User

# import sys
# from django.core.wsgi import get_wsgi_application
# sys.path.extend(['Path_to_your_django_project',])
# os.environ.setdefault("DJANGO_SETTINGS_MODULE","Name_Of_Your_Django_Project.settings")
# application = get_wsgi_application()

# Create your tests here.

if __name__=='__main__':
    
    tb=TaskBatch()
    tb.save()
    for user in User.objects.all():
        try:
            if user.project:
                ts=TaskState()
                ts.task_batch=tb
                ts.task_state=taskState_choice[0][0]
                ts.user=user
                ts.email=user.email
                ts.project=user.project
                ts.save()
        except Exception, err:
            pass
