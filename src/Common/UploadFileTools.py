#!/usr/bin/env python
#_*_coding:utf-8_*_
'''
2016-1-4 上午8:21:55
XingTong
'''
import sys,os,time,shutil,cPickle
import DepWorkSite.settings as settings
from __builtin__ import str

#修改系统的默认编码模式为utf-8
reload(sys)
sys.setdefaultencoding('utf-8')

        
def getExistsFiles(dirPath):
    '''
        得到文件夹中存在的文件列表
        @param uploadDirPath:文件夹的路径
        @return: 文件夹中存在的文件列表 
    '''
    existsFileList=[]
    if dirPath:
        dirFullPath=os.path.join(settings.UPLOAD_DIR,'upload',dirPath)  #得到文件夹的路径
#             print settings.UPLOAD_DIR,dirFullPath
        if os.path.exists(dirFullPath) and os.path.isfile(dirFullPath):
            existsFileList.append([os.path.basename(dirFullPath),dirPath])
        elif os.path.exists(dirFullPath) and os.path.isdir(dirFullPath):
            existsFileList=[[fileName,dirPath] for fileName in os.listdir(dirFullPath)]
    return sorted(existsFileList,key=lambda x:x[0])        
            
 
def deleteFile(dirPath,fileName):
    '''
        删除文件
    @param  fileName: 待删除文件的文件名
    '''
    fileFullPath=os.path.join(settings.UPLOAD_DIR,'upload',dirPath,fileName)  #得到文件的路径
    if os.path.exists(fileFullPath) and os.path.isfile(fileFullPath):  #如果存在且是文件
        os.remove(fileFullPath)
        
        
def createUploadDir():
    '''
        创建上传文件夹的名称
    '''
    return  os.path.join(time.strftime('%Y%m%d'),time.strftime('%H%M%S'))
    
def getUploadDirPath(uploadDirPath=None):
    '''
        得到上传文件夹的路径
    '''
    if not uploadDirPath:
        uploadDirPath=createUploadDir() #得到上传文件夹的名称
    uploadDirPath=os.path.join(settings.UPLOAD_DIR,'upload',uploadDirPath)  #得到上传文件夹的路径
    if not os.path.exists(uploadDirPath):
        os.makedirs(uploadDirPath)
    return uploadDirPath

def getUploadFilePath(uploadDirPath,uploadFileName):
    '''
        得到上传文件的路径
    @param uploadDirPath: 上传文件夹的路径
    @param uploadFileName: 上传文件的文件名
    '''
    uploadFilePath=os.path.join(getUploadDirPath(uploadDirPath),uploadFileName)
    if os.path.exists(uploadFilePath):
        (fileName,extName)=os.path.splitext(uploadFileName)
        fullFileName=''.join(fileName,'_',time.strftime('%Y%m%d%H%M%S'),extName)
        uploadFilePath=getUploadFilePath(uploadDirPath,fullFileName)
    return uploadFilePath

def saveFile(fileDic,uploadDirPath=None):
    '''
        在磁盘上持久化文件
    @param fileDic:
    @param uploadDirPath:上传后的文件夹路径  
    '''
    dirFullPath=getUploadDirPath(uploadDirPath)
    if fileDic:
        for name,uploadFile in fileDic.items():
            uploadFilePath=getUploadFilePath(dirFullPath, uploadFile.name)
            with open(uploadFilePath,'wb+') as destFile:
                for chunk in uploadFile.chunks():
                    destFile.write(chunk)
    return dirFullPath[-15:]
    

def deleteDir(deleteDirPath=None):
    '''
        删除文件夹
    @param deleteDirPath: 待删除的文件夹路径
    ''' 
    if deleteDirPath:
        deleteDirFullPath=os.path.join(settings.UPLOAD_DIR,'upload',deleteDirPath)
        if os.path.exists(deleteDirFullPath) and os.path.isfile(deleteDirFullPath):  #如果是文件
            os.remove(deleteDirFullPath)
        if os.path.exists(deleteDirFullPath) and os.path.isdir(deleteDirFullPath):  #如果是文件夹
            shutil.rmtree(deleteDirFullPath)  #删除文件夹
    

def getFile(dirPath,fileName,chunk_size=512):
    '''
    得到文件数据
    @param dirPath:文件夹路径
    @param fileName:文件名 
    @param chunk_size:分块大小
    @return: 生成器，返回数据 
    '''
    fileFullPath=os.path.join(settings.UPLOAD_DIR,'upload',dirPath,fileName)
    if os.path.exists(fileFullPath) and os.path.isfile(fileFullPath):
        with open(fileFullPath,'rb+') as f:
            while True:
                c=f.read(chunk_size)
                if c:
                    yield c
                else:
                    break