from django.test import TestCase
from django.contrib.auth.models import Group
from ProjectManagement.models import Project
from UserManagement.models import CustomUser
from django.contrib.auth.models import Permission
from Sys.models import *

# Create your tests here.
class SysTestCase(TestCase):
    
    def setUp(self):
        Project.objects.create(projectName='project1',projectDescribe='project1')
    
    def test_add_user(self):
        
        project=Project.objects.get(projectName='project1')
        CustomUser.objects.create(username="lion", project=project)
        users=CustomUser.objects.filter(username="lion")
        self.assertIsNotNone(users[0])
        self.assertEqual(users[0].username,'lion')
        
    def test_modify_user(self):
        project=Project.objects.get(projectName='project1')
        CustomUser.objects.create(username="lion", project=project)
        users=CustomUser.objects.filter(username="lion")
        user=users[0]
        user.username='tiger'
        user.save()
        users=CustomUser.objects.filter(username="tiger")
        self.assertIsNotNone(users[0])
        self.assertEqual(users[0].username,'tiger')
        
    def test_delete_user(self):
        project=Project.objects.get(projectName='project1')
        CustomUser.objects.create(username="lion", project=project)
        users=CustomUser.objects.filter(username="lion")
        users[0].delete()
        users=CustomUser.objects.filter(**{r'username':'lion'})
        self.assertIsNotNone(users)
        self.assertEqual(len(users),0)
        
    def test_add_permission(self):
        permission= Permission.objects.create(name='p1',content_type_id='1')
        permissions=Permission.objects.filter(**{'name':'p1'})
        self.assertIsNotNone(permissions)
        self.assertGreater(len(permissions), 0)
        
    def test_modify_permission(self):
        permission= Permission.objects.create(name='p1',content_type_id='1')
        permission.name='p2'
        permission.save()
        permissions=Permission.objects.filter(**{'name':'p2'})
        self.assertIsNotNone(permissions)
        self.assertGreater(len(permissions), 0)
        
    def test_delete_permission(self):
        Permission.objects.create(name='p1',content_type_id='1')
        permissions=Permission.objects.filter(**{'name':'p1'})
        permissions[0].delete()
        permissions=Permission.objects.filter(**{'name':'p1'})
        self.assertIsNotNone(permissions)
        self.assertEqual(len(permissions), 0)
        
    def test_add_group(self):
        Group.objects.create(name='g1')
        groups=Group.objects.filter(**{'name':'g1'})
        self.assertIsNotNone(groups)
        self.assertGreater(len(groups), 0)
        
    def test_modify_group(self):
        group=Group.objects.create(name='g1')
        group.name='g2'
        group.save()
        groups=Group.objects.filter(**{'name':'g2'})
        self.assertIsNotNone(groups)
        self.assertGreater(len(groups), 0)
        
    def test_delete_group(self):
        Group.objects.create(name='g1')
        groups=Group.objects.filter(**{'name':'g1'})
        groups[0].delete()     
        groups=Group.objects.filter(**{'name':'g1'})
        self.assertIsNotNone(groups)
        self.assertEqual(len(groups), 0)