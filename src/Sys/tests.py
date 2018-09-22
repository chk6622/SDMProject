from django.test import TestCase
from django.contrib.auth.models import User,Group
from Sys.models import *

# Create your tests here.
class SysTestCase(TestCase):
    
    def test_sys(self):
        Project.objects.create(projectName='project1')
        project=Project.objects.get(projectName='project1')
        self.assertIsNotNone(project)
        User.objects.create(username="lion", project=project)
        users=User.objects.filter(username="lion")
        self.assertIsNotNone(users[0])
        self.assertEqual(users[0].username,'lion')
        users[0].delete()
        users=User.objects.filter(**{r'username':'lion'})
        self.assertIsNotNone(users)
        self.assertEqual(len(users),0)
        Permission.objects.create(name='p1',content_type_id='1')
        permissions=Permission.objects.filter(**{'name':'p1'})
        self.assertIsNotNone(permissions)
        self.assertGreaterEqual(len(permissions), 0)
        Group.objects.create(name='g1')
        groups=Group.objects.filter(**{'name':'g1'})
        self.assertIsNotNone(groups)
        self.assertGreaterEqual(len(groups), 0)
        groups[0].delete()
        permissions[0].delete()
        permissions=Permission.objects.filter(**{'name':'p1'})
        self.assertIsNotNone(permissions)
        self.assertEqual(len(permissions), 0)
        groups=Group.objects.filter(**{'name':'g1'})
        self.assertIsNotNone(groups)
        self.assertEqual(len(groups), 0)