#!/usr/bin/env python
#_*_coding:utf-8_*_
'''
2015-10-15 下午2:18:09
XingTong
split pages tools
'''
import sys,time,os
import logging
import traceback



logger=logging.getLogger('django')
def getSplitPageParams(pageSize,pageNum,totalSize):
    '''
    得到查询分页参数
    @param pageSize:每页记录数
    @param pageNum:页数
    @param totalSize:总记录数
    @return: (本页开始记录数,本页结束记录数)   
    '''
    defaultPageNum=1  #默认页数
    defaultPageSize=10  #默认每页记录数
    try:
        pageSize=int(pageSize)  #每页记录数
    except Exception,e:
        pageSize=defaultPageSize
    try:
        pageNum=int(pageNum)  #页数
    except Exception,e:
        pageNum=defaultPageNum
    if pageSize<=0:
        pageSize=defaultPageSize
    if pageNum<=0:
        pageNum=defaultPageNum
    (maxPageNum,lastSize) = divmod(totalSize, pageSize) #得到最大页数和最后一页的记录数
    if lastSize>0:  #最后一页记录数不为0，最大页数加1
        maxPageNum+=1
    
    if lastSize==0 and maxPageNum>0:
            lastSize=pageSize
   
    if pageNum>=maxPageNum>=1:
        pageNum=maxPageNum
        
    beginSize=(pageNum-1)*pageSize  #开始记录数
#     endSize=beginSize+lastSize  #结束记录数
    if pageNum==maxPageNum:
        endSize=beginSize+lastSize  #结束记录数
    else:
        endSize=beginSize+pageSize  #结束记录数
    nextPageNum=pageNum+1
    prevPageNum=pageNum-1
    return (pageNum,pageSize,beginSize,endSize,maxPageNum,nextPageNum,prevPageNum)

def getRequestParam(request):
    requestDic=request.GET
    tmpDic={}
    tmpDic.update(requestDic)
    for k,v in tmpDic.items():
        if v and v[0]:
            tmpDic.update({k:v[0]})
        else:
            tmpDic.pop(k)
    paramDic=request.session.get('GET_PARAM')
    if not paramDic or tmpDic.get('isFlush'):
        paramDic={}
    paramDic.update(tmpDic) 
    request.session['GET_PARAM']=paramDic
    return paramDic

def getWhereParam(request,whereParam,postParam=None,getParam=None):
    '''
    得到字段的查询条件
    @param request:
    @param whereParam:字段查询参数，例如'xxx__contains'
    @param postParam:post请求中的参数名称
    @param getParam:get请求中的参数名称
    @return 如果参数为None则返回None，否则返回形如'{whereParam，paramValue}'的字典  
    '''
    param=None
    returnDic=None
    if postParam:
        param=request.POST.get(postParam,None)
    elif getParam:
        param=request.GET.get(getParam,None)
    if param:
        returnDic={whereParam:param}
    return returnDic

def getFilterDic(request,filterDic,whereParam,paramName=None):
    '''
    得到model查询需要的filterDic
    @param request:
    @param filterDic
    @param whereParam:字段查询参数，例如'xxx__contains'
    @param postParam:post请求中的参数名称
    @param getParam:get请求中的参数名称
    @return: filterDic
    '''
#     whereDic=getWhereParam(request, whereParam, postParam,getParam)
    paramDic=request.session.get('GET_PARAM')
    value=paramDic.get(paramName,None)
    if value:
        filterDic.update({whereParam:value})

def clamSelf(func):
    '''
    装饰器，打印执行方法的名称
    '''
    def inner(request):
        
#         logger.info( "enter '%s' method" % func.__name__)
#         print "enter '%s' method" % func.__name__
        result=None
        try:
            result=func(request)
        except Exception,e:
            logger.exception(e)
        return result
    return inner

