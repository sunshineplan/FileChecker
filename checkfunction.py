#!/usr/bin/python3
# coding:utf-8

from iolib import file2list
from iolib import sort_data
from iolib import save_original

def chk_repeat(file1,file2=''):
    data1=file2list(file1)
    save_original(file1,data1)
    if file2!='':
        data2=file2list(file2)
        save_original(file2,data2)
    result=[]
    if file2=='':
        for i in data1:
            if data1.count(i)!=1:
                result.append(str(i)+'出现了'+str(data1.count(i))+'次')
                result=list(set(result))
    else:
        data2=file2list(file2,display_warning='off',remove_duplicate='on')
        for i in data2:
            if data1.count(i)!=0:
                result.append(i)
    result=sort_data(result)
    return result

def compare(file1,file2,data_type='file'):
    if data_type=='file':
        data1=file2list(file1)
        data2=file2list(file2)
    else:
        data1=file1
        data2=file2
    count=0
    result=[]
    while count<len(data1):
        if data1[count] not in data2:
            result.append(data1[count])
        count+=1
    return result

def chk_consecutive(filename):
    data=file2list(filename)
    int_list=sorted(list(map(int,data)))         #将字符数组转换成数字数组
    start=int_list[0]
    end=int_list[-1]
    full_list=list(range(start,end+1))
    result=compare(full_list,int_list,data_type='list')
    result=list(map(str,result))
    if result!=[]:
        str_list=list(map(str,int_list))
        save_original(filename,str_list)
    return result
    
    
    
    
