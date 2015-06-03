#!/usr/bin/python3
# coding:utf-8

from iolib import file2list
from iolib import list2file

def chk_repeat(filename):
    file=file2list(filename)
    repeat=[]
    i=filename.rindex('.')
    for a in file:
        if file.count(a)!=1:
            repeat.append(str(a)+'重复了'+str(file.count(a))+'次')
    output=list(set(repeat))#删除重复值
    output.sort()
    if output!=[]:#如有重复，将去重后文件输出，文件名加上"_changed"
        changed=list(set(file))
        changed.sort()
        changedfile=list2file(changed,filename[:i]+'_changed'+filename[i:])
    return output

def compare(file1,file2):
    f1=file2list(file1)
    f2=file2list(file2)
    c=0
    result=[]
    while c<len(f1):
        if f1[c] not in f2:
            result.append(f1[c])
        c+=1
    return result
