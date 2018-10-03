# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from ProjectManagement.models import Project

# Create your tests here.


class ProjectTestCase(TestCase):
    
    def test_project(self):
        Project.objects.create(projectName='project1')
        projects=Project.objects.filter(projectName='project1')
        self.assertTrue(projects)
        self.assertGreater(len(projects), 0)
        project=projects[0]
        project.projectName='project2'
        project.save()
        projects=Project.objects.filter(projectName='project2')
        self.assertTrue(projects)
        self.assertGreater(len(projects), 0)
        projects[0].delete()
        projects=Project.objects.filter(projectName='project2')
        self.assertIsNone(projects)
        self.assertEqual(len(projects), 1)

