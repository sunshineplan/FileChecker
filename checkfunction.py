#!/usr/bin/python3
# coding:utf-8

from iolib import file2list
from iolib import sortdata
from iolib import saveoriginal

def chk_repeat(file1,file2=''):
    f1=file2list(file1,displayinfo='off')
    count=0
    repeat=[]
    if file2=='':
        for a in f1:
            if f1.count(a)!=1:
                repeat.append(str(a)+'出现了'+str(f1.count(a))+'次')
    else:
        f2=file2list(file2,displayinfo='off',removeduplicate='on')
        for a in f2:
            if f1.count(a)!=0:
                repeat.append(a)
    if repeat!=[]:
        f2=file2list(file2,displayinfo='off')
        saveoriginal(file1,f1)
        saveoriginal(file2,f2)
    repeat=sortdata(repeat)
    return repeat

def compare(file1,file2,displayinfo='on',chk_have='off',data_type='file'):
    if data_type!='file':
        f1=file1
        f2=file2
    else:
        if displayinfo=='on':
            f1=file2list(file1)
            f2=file2list(file2)
        else:
            f1=file2list(file1,displayinfo='off')
            f2=file2list(file2,displayinfo='off')
    if chk_have=='on':
        if len(f1)>len(f2):
            print(file1+'比'+file2+'大，检查'+file2+'是否包含于'+file1)
            tmp=f1
            f1=f2
            f2=tmp
        else:
            print(file1+'不比'+file2+'大，检查'+file1+'是否包含于'+file2)
    count=0
    result=[]
    while count<len(f1):
        if f1[count] not in f2:
            result.append(f1[count])
        count+=1
    return result

def chk_continuity(filename):
    file=file2list(filename)
    intlist=list(map(int,file))#将字符数组转换成数字数组
    start=intlist[0]
    end=intlist[-1]
    goal=list(range(start,end+1))
    result=compare(goal,intlist,'off','off','list')
    return result
    
    
    
    
