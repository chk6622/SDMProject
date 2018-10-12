# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
import django
from django.test import TestCase
from HappyManagement.models import TaskBatch,TaskState,taskState_choice

import sys
import os


from django.contrib.auth.models import User
from UserManagement.models import CustomUser
from django.db.models import Q
from django.db import transaction
from ProjectManagement.models import Project


class HappyManagementTest(TestCase):
    def setUp(self):
        TaskState.objects.filter(task_state='1').update(task_state='3')  #update all records which are undone into timeout
    
#     def test_happy_management(self):
#         tb=TaskBatch()
#         tb.save()
# 
#         ts=TaskState()
#         ts.task_batch=tb
#         ts.task_state=taskState_choice[0][0]
#         Project.objects.create(projectName='project1',projectDescribe='project1')
#         project=Project.objects.get(projectName='project1')
#         self.assertIsNotNone(project)
#         
#         
#         CustomUser.objects.create(username="lion",email='x1980p@gmail.com',project=project)
#         users=CustomUser.objects.filter(username="lion")
#         ts.user=users[0]
#         ts.email=users[0].email
#         ts.project=users[0].project
#         ts.save()
#         taskStates=TaskState.objects.filter(email='x1980p@gmail.com')
#         self.assertIsNotNone(taskStates)
#         self.assertGreater(len(taskStates), 0)
#         
#         
#         taskStates[0].email='chk6622@auts.zc.com'
#         taskStates[0].save()
#         taskStates=TaskState.objects.filter(user=users)
#         self.assertIsNotNone(taskStates)
#         self.assertGreater(len(taskStates), 0)
#         self.assertEqual(taskStates[0].email, 'chk6622@auts.zc.com')
#         
#         
#         ts_id=taskStates[0].id
#         taskStates[0].delete()
#         taskStates=TaskState.objects.filter(id=ts_id)
#         self.assertIsNotNone(taskStates)
#         self.assertEquals(len(taskStates), 0)
#         
#         tb_id=tb.id
#         tb.delete()
#         
#         taskBatchs=TaskBatch.objects.filter(id=tb_id)
#         self.assertIsNotNone(taskBatchs)
#         self.assertEquals(len(taskBatchs), 0)
        
    def test_add_task_batch(self):

        tb=TaskBatch()
        tb.save()
        taskBatchs=TaskBatch.objects.filter(id=tb.id)
        self.assertIsNotNone(taskBatchs)
        self.assertEqual(len(taskBatchs), 1)

    
    def test_delete_task_batch(self):
        tb=TaskBatch()
        tb.save()
        
        tb_id=tb.id
        tb.delete()
        
        taskBatchs=TaskBatch.objects.filter(id=tb_id)
        self.assertIsNotNone(taskBatchs)
        self.assertEquals(len(taskBatchs), 0)
        
    def test_add_task_state(self):
        tb=TaskBatch()
        tb.save()

        ts=TaskState()
        ts.task_batch=tb
        ts.task_state=taskState_choice[0][0]
        project=Project.objects.create(projectName='project1',projectDescribe='project1')
        
        
        user=CustomUser.objects.create(username="lion",email='x1980p@gmail.com',project=project)
        ts.user=user
        ts.email=user.email
        ts.project=user.project
        ts.save()
        taskStates=TaskState.objects.filter(email='x1980p@gmail.com')
        self.assertIsNotNone(taskStates)
        self.assertGreater(len(taskStates), 0)
        
        
    def test_modify_task_state(self):
        tb=TaskBatch()
        tb.save()

        ts=TaskState()
        ts.task_batch=tb
        ts.task_state=taskState_choice[0][0]
        project=Project.objects.create(projectName='project1',projectDescribe='project1')
        
        
        user=CustomUser.objects.create(username="lion",email='x1980p@gmail.com',project=project)
        ts.user=user
        ts.email=user.email
        ts.project=user.project
        ts.save()
        taskStates=TaskState.objects.filter(email='x1980p@gmail.com')
        self.assertIsNotNone(taskStates)
        self.assertGreater(len(taskStates), 0)
        
        
        taskStates[0].email='chk6622@auts.zc.com'
        taskStates[0].save()
        taskStates=TaskState.objects.filter(user=user)
        self.assertIsNotNone(taskStates)
        self.assertGreater(len(taskStates), 0)
        self.assertEqual(taskStates[0].email, 'chk6622@auts.zc.com')
        
    def test_delete_task_state(self):
        tb=TaskBatch()
        tb.save()

        ts=TaskState()
        ts.task_batch=tb
        ts.task_state=taskState_choice[0][0]
        
        Project.objects.create(projectName='project1',projectDescribe='project1')
        project=Project.objects.get(projectName='project1')
        
        
        user=CustomUser.objects.create(username="lion",email='x1980p@gmail.com',project=project)
        ts.user=user
        ts.email=user.email
        ts.project=user.project
        ts.save()
        
        
        ts_id=ts.id
        ts.delete()
        taskStates=TaskState.objects.filter(id=ts_id)
        self.assertIsNotNone(taskStates)
        self.assertEquals(len(taskStates), 1)
    
