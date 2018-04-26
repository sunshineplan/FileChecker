#!/usr/bin/python3
# coding:utf-8

from iolib import file2list
from iolib import sort_data
from iolib import save_original
from iolib import precheck
from time import time

def chk_repeat(file1,file2='',data_type='file',display_warning='on'):
    start_time=time()
    if data_type=='file':
        data1=file2list(file1)
        if display_warning=='on':
            save_original(file1,data1)
        if file2!='':
            data2=file2list(file2)
            if display_warning=='on':
                save_original(file2,data2)
    else:
        data1=precheck(file1)
        if file2!='':
            data2=precheck(file2)
    result=[]
    if file2=='':
        tmp=''
        for i in data1:
            if i==tmp:
                continue
            if data1.count(i)!=1:
                result.append(str(i)+'\t出现了'+str(data1.count(i))+'次')
            tmp=i
    else:
        data2=list(set(data2))
        for i in data2:
            if data1.count(i)!=0:
                result.append(i)
    result=sort_data(result)
    elapsed_time=time()-start_time
    return result,elapsed_time

def compare(file1,file2,data_type='file',display_warning='on'):
    start_time=time()
    if data_type=='file':
        if display_warning=='on':
            data1=file2list(file1)
            data2=file2list(file2)
            save_original(file1,data1)
            save_original(file2,data2)
        else:
            data1=file2list(file1,display_warning='off')
            data2=file2list(file2,display_warning='off')
    else:
        data1=file1
        data2=file2
    result=data1.copy()
    for i in data2:
        if i in result:
            result.remove(i)
    elapsed_time=time()-start_time
    return result,elapsed_time

def chk_consecutive(filename,data_type='file'):
    start_time=time()
    if data_type=='file':
        data=file2list(filename)
    else:
        data=filename
    int_list=sorted(list(map(int,data)))         #将字符数组转换成数字数组
    start=int_list[0]
    end=int_list[-1]
    full_list=list(range(start,end+1))
    result,_=compare(full_list,int_list,data_type='list')
    result=list(map(str,result))
    if result!=[] and data_type=='file':
        str_list=list(map(str,int_list))
        save_original(filename,str_list)
    elapsed_time=time()-start_time
    return result,elapsed_time
    
    
    
    
