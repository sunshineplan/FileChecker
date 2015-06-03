#!/usr/bin/python3
# coding:utf-8

from iolib import file2list
from iolib import list2file
from iolib import precheck

def chk_repeat(filename):
    file=file2list(filename)
    originalfile=file2list(filename,'off')
    count=0
    for line in originalfile:
        line=line.strip('\n')
        originalfile[count]=line
        count+=1
    repeat=[]
    i=filename.rindex('.')
    for a in file:
        if file.count(a)!=1:
            repeat.append(str(a)+'重复了'+str(file.count(a))+'次')
    output=list(set(repeat))#删除重复值
    output.sort()
#如有重复，将去重后文件输出，原文件名加上"_original"
    if output!=[] or file!=originalfile:
        changed=list(set(file))
        changed.sort()
        list2file(originalfile,filename[:i]+'_original'+filename[i:])
        list2file(changed,filename)
    return output

def compare(file1,file2,displayinfo='on'):
    if displayinfo=='on':
        f1=file2list(file1)
        f2=file2list(file2)
    else:
        f1=file2list(file1,displayinfo='off')
        f2=file2list(file2,displayinfo='off')
    count=0
    result=[]
    while count<len(f1):
        if f1[count] not in f2:
            result.append(f1[count])
        count+=1
    return result
