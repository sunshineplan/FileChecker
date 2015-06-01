#!/usr/bin/python3
# coding:utf-8

from iolib import file2list
from iolib import list2file

def chk_repeat(filename):
    file=file2list(filename)
    repeat=[]
    for a in file:
        if file.count(a)!=1:
            repeat.append(str(a)+'重复了'+str(file.count(a))+'次')
    output=list(set(repeat))#删除重复值
    output.sort()
    if output!=[]:
        changed=list(set(file))#将去重后的文件输出，文件名在原来的基础上加"_changed"后缀
        changed.sort()
        changedfile=list2file(changed,filename[:filename.rindex('.')]+'_changed'+filename[filename.rindex('.'):])
    return output

def compare(file1,file2):
    print('file1要包含file2')
    c1=0
    c2=0
    result=[]
    while c2<len(file2):
        if file1[c1]==file2[c2]:
            c1+=1
            c2+=1
        else:
            result.append(file1[c1])
            c1+=1
    return result
