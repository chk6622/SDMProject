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
from UserManagement.models import UserManageForm
import logging
# Create your views here.
queryUrl='user_management/queryUser.html'  #查询模板
addUrl='user_management/addUser.html'      #添加模板
editUrl='user_management/editUser.html'    #编辑模板
ModelKlass=User     #模型类
FormKlass=UserManageForm  #表单类
queryFilterParams=[]      #数据查询参数列表
queryFilterParams.append(('first_name__contains','first_name_qry'))
queryFilterParams.append(('last_name__contains','last_name_qry'))


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
#     perms=request.get_model_perms()
#     print isSuperuser,project,perms
    paramDic=getRequestParam(request)
    pageSize=paramDic.get('pageSize')
    pageNum=paramDic.get('pageNum')
    
    filterDic={}
    for filterParam in queryFilterParams:  #add query params
        getFilterDic(request, filterDic, filterParam[0], filterParam[1])
        
    if not isSuperuser:
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


@login_required
def addOrEdit(request):
    logger.debug("'%s(%s%s)' execute method" % (request.user.username,request.user.last_name,request.user.first_name))
    id=request.GET.get('id',None)
    if not id:
        id=request.POST.get('id',None)
    templateDir=addUrl
    if id:
        optObj=ModelKlass.objects.get(id=id)
        if optObj: 
            optObjForm=FormKlass(instance=optObj)
            templateDir=editUrl
    else:
        optObjForm=FormKlass()  
    return render(request, templateDir, locals()) 


@login_required
def saveOrUpdate(request):
    userInfo='%s(%s%s)' % (request.user.username,request.user.last_name,request.user.first_name)
    logger.debug("'%s' execute method" % userInfo)
    returnTemplate=None
    optObj=None
    uploadFileList=None
#     addForm=None
    if request.method=='POST':
        id=request.POST.get('id',None)
        if id:
            optObj=ModelKlass.objects.get(id=id)
        if optObj:
            optObjForm=FormKlass(request.POST,instance=optObj)           
            returnTemplate=editUrl
        else:
            optObjForm=FormKlass(request.POST)
            returnTemplate=addUrl
#             addForm=FormKlass()
        if optObjForm.is_valid():
            try:
                optObj=optObjForm.save()
                messages.info(request,'save success!')
            except Exception,e:
                logger.exception(e)
                messages.error(request,'save fail!')
    else:
        optObjForm=FormKlass()
        returnTemplate=addUrl
    return render(request, returnTemplate, locals())