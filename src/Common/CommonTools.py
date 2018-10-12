#!/usr/bin/env python
#coding: utf-8
'''
Created on Oct 12, 2018

@author: Chunlu Hu
'''

#!/usr/bin/env python
#coding: utf-8
'''
Created on Oct 12, 2018

@author: Chunlu Hu
'''

import socket
from datetime import datetime
from datetime import timedelta

SO_BINDTODEVICE=25

def get_host_ip():
    '''
    get the host ip
    @return: the host ip
    '''
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
#     ip='localhost'
    return ip

def get_free_port(iface=None):
    #  iface parameters is the interface of Linux network card address，for example (eth0,wlan0)，This parameter just supports Linux, and needs the privilege of root
    s = socket.socket()
    if iface:
        s.setsockopt(socket.SOL_SOCKET, SO_BINDTODEVICE, bytes(iface,'utf8'))
    s.bind(('',0))
    port = s.getsockname()[1]
    s.close()
    return port

def calcute_datetime(orginDatetime=datetime.now(),minutes=0):
    return orginDatetime + timedelta(minutes=minutes)

notifyTimes={0:5,1:10,2:15,3:20,4:25,5:30}

def get_postpone_time(notify_count=0):
    pReturn=30
    pt = notifyTimes.get(notify_count)
    if pt:
        pReturn = pt
    return pReturn
    

if __name__=='__main__':
    time1 = datetime.now()
    print 'today is %s' % time1.strftime('%Y-%m-%d %H:%M')
    aDay = timedelta(minutes=1)
    time2 = time1 + aDay
    print time2.strftime('%Y-%m-%d %H:%M')
    print time2>=time1
