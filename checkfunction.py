#!/usr/bin/python3
# coding:utf-8

from iolib import file2list
from iolib import list2file
from iolib import precheck
from iolib import sortdata

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
    output=sortdata(output)
#如有重复，将去重后文件输出，原文件名加上"_original"
    if output!=[] or file!=originalfile:
        changed=list(set(file))
        changed=sortdata(changed)
        list2file(originalfile,filename[:i]+'_original'+filename[i:])
        list2file(changed,filename)
    return output

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
    
    
    
    
