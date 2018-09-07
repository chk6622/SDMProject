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
# Create your views here.
queryUrl='happy_level_management/queryHappyLevel.html'  
addUrl='happy_level_management/addHappyLevel.html'      
editUrl='happy_level_management/editHappyLevel.html'   
ModelKlass=HappyLevel     
FormKlass=HappyLevelForm  
queryFilterParams=[]      
queryFilterParams.append(('create_user__contains','create_user_qry'))
queryFilterParams.append(('project','project_qry'))
queryFilterParams.append(('personal_happy_level__contains','personal_happy_level_qry'))
queryFilterParams.append(('project_happy_level__contains','project_happy_level_qry'))
queryFilterParams.append(('create_time__gte','b_create_time'))
queryFilterParams.append(('create_time__lte','e_create_time'))



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
        if optObj: #update
            optObjForm=FormKlass(request.POST,instance=optObj)           
            returnTemplate=editUrl
        else: #add
            optObjForm=FormKlass(request.POST)
            
            returnTemplate=addUrl
#             addForm=FormKlass()
        if optObjForm.is_valid():
            try:
                if not optObjForm.instance.id: #add
                    optObjForm.instance.create_user=request.user
                    optObjForm.instance.update_user=request.user
                else:  #edit
                    optObjForm.instance.update_user=request.user
                optObjForm.instance.project=request.user.project
                optObj=optObjForm.save()
                messages.info(request,'save success!')
            except Exception,e:
                logger.exception(e)
                messages.error(request,'save fail!')
    else:
        optObjForm=FormKlass()
        returnTemplate=addUrl
    return render(request, returnTemplate, locals())


@login_required
def exportData(request):
    logger.debug("'%s(%s%s)' execute method" % (request.user.username,request.user.last_name,request.user.first_name))
    isSuperuser=None
    project=None
    try:
        isSuperuser=request.user.is_superuser
        project=request.user.project
    except Exception, err:
        pass
    fileName='Happy level %s.csv' % datetime.datetime.now().strftime(settings.GLOBAL_DATE_FORMAT)

    filterDic={}
    for filterParam in queryFilterParams:
        getFilterDic(request, filterDic, filterParam[0], filterParam[1])
        
    if not isSuperuser and project:
        filterDic.update({'project':project})

    response=StreamingHttpResponse(getObj(filterDic))
    response['Content-Type']='application/octet-stream'
    response['Content-Disposition']="attachment;filename={0}".format(urlquote(fileName))
    return response

            
def getObj(filterDic):
    logger.debug("enter 'getObj' method")
    isExportTitle=False
    totalSize=ModelKlass.objects.filter(**filterDic).count()
    if totalSize>0:
        queryResultList=ModelKlass.objects.filter(**filterDic)[0:totalSize]
        for optObj in queryResultList:
            (attrlabels,rList)=optObj.getFormatObj()
            if not isExportTitle:
                row=','.join(attrlabels)
                row='%s\r\n' % row
                yield row
                isExportTitle=True
            if isinstance(optObj,ModelKlass):
                row=','.join(map(lambda x:x.replace('\r\n',''),rList))
                row='%s\r\n' % row
                yield row
    else:
        yield 'No data!'