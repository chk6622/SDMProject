#!/usr/bin/env python
#coding: utf-8
'''
Created on Oct 4, 2018

@author: xingtong
'''

import socket
 
def get_host_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
 
    return ip
