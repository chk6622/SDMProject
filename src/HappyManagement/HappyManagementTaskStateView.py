# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

import sys
from django.shortcuts import render_to_response
from Common.ViewTools import *
from django.views.decorators.csrf import csrf_protect
from django.template import RequestContext
import SDMProject.settings as settings
import time
from django.http import StreamingHttpResponse,HttpResponse
from django.utils.http import urlquote
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from __builtin__ import isinstance
from django.contrib.auth.models import User
from HappyManagement.models import *
import logging

from django.db import transaction
# Create your views here.
queryUrl='happy_level_management/queryHappyLevelTaskState.html'  
addUrl=''      
editUrl=''   
errorUrl=''
submitUrl=''
submitSuccessUrl=''
ModelKlass=TaskState     
FormKlass=TaskStateForm  
queryFilterParams=[]      
queryFilterParams.append(('email__contains','email_qry'))
queryFilterParams.append(('task_state','task_state_qry'))
queryFilterParams.append(('task_batch__create_time__gte','b_create_time'))
queryFilterParams.append(('task_batch__create_time__lte','e_create_time'))
queryFilterParams.append(('task_state','task_state_qry'))
queryFilterParams.append(('project_id','project_qry'))



logger = logging.getLogger(__name__)

@login_required
def query(request):
    logger.debug("'%s(%s%s)' execute method" % (request.user.username,request.user.last_name,request.user.first_name))
    isSuperuser=None
    project=None
    try:
        isSuperuser=request.user.is_superuser
        project=request.user.project
    except Exception, err:
        pass

    paramDic=getRequestParam(request)
    pageSize=paramDic.get('pageSize')
    pageNum=paramDic.get('pageNum')
    
    filterDic={}
    for filterParam in queryFilterParams:  #add query params
        getFilterDic(request, filterDic, filterParam[0], filterParam[1])
    
    if not isSuperuser and project:
        filterDic.update({'project':project})
        
    
    queryForm=FormKlass(paramDic)
    totalSize=ModelKlass.objects.filter(**filterDic).count()
    (pageNum,pageSize,beginSize,endSize,maxPageNum,nextPageNum,prevPageNum)=getSplitPageParams(pageSize,pageNum,totalSize)
    queryResultList=[]
    if totalSize:
        queryResultList=ModelKlass.objects.filter(**filterDic)[beginSize:endSize]
        beginSize+=1  #start record number add 1, used to list display
    else:
        pageNum=0
        pageSize=0
        beginSize=0
        endSize=0
        maxPageNum=0
        nextPageNum=0
        prevPageNum=0
    return render(request, queryUrl, locals())
