# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.test import TestCase
from CommonTools import *




class CommonToolsTest(TestCase):
    
    def test_host_ip(self):
        hostIp=get_host_ip()
        print hostIp
        self.assertIsNotNone(hostIp, hostIp)
        
    def test_free_port(self):
        port=get_free_port()
        print port
        self.assertIsNotNone(port, port)
        
    def test_calcute_time(self):
        now=datetime.now()
        targetTime=calcute_datetime(now, 5)
        self.assertGreater(targetTime, now)
        targetTime=calcute_datetime(now, -5)
        self.assertLess(targetTime, now)
