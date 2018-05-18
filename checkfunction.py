#!/usr/bin/python3
# coding:utf-8

from iolib import file2list
from iolib import sort_data
from iolib import save_original
from iolib import precheck
from time import time

def chk_duplicates(data1,data2='',data_type='file',display_warning='on'):
    start_time=time()
    if data_type=='file':
        list1=file2list(data1)
        if display_warning=='on':
            save_original(data1,list1)
        if data2!='':
            list2=file2list(data2)
            if display_warning=='on':
                save_original(data2,list2)
    else:
        list1=precheck(data1)
        if data2!='':
            list2=precheck(data2)
    result=[]
    if data2=='':
        tmp=''
        for i in list1:
            if i==tmp:
                continue
            if list1.count(i)!=1:
                result.append(str(i)+'\t出现了'+str(list1.count(i))+'次')
            tmp=i
    else:
        list2=list(set(list2))
        for i in list2:
            if list1.count(i)!=0:
                result.append(i)
    result=sort_data(result)
    elapsed_time=time()-start_time
    return result,elapsed_time

def compare(data1,data2,data_type='file',display_warning='on'):
    start_time=time()
    if data_type=='file':
        if display_warning=='on':
            list1=file2list(data1)
            list2=file2list(data2)
            save_original(data1,list1)
            save_original(data2,list2)
        else:
            list1=file2list(data1,display_warning='off')
            list2=file2list(data2,display_warning='off')
    else:
        list1=data1
        list2=data2
    result=list1.copy()
    for i in list2:
        if i in result:
            result.remove(i)
    elapsed_time=time()-start_time
    return result,elapsed_time

def chk_consecutive(data,data_type='file'):
    start_time=time()
    if data_type=='file':
        list_data=file2list(data)
    else:
        list_data=data
    int_list=sorted(list(map(int,list_data)))         #将字符数组转换成数字数组
    start=int_list[0]
    end=int_list[-1]
    full_list=list(range(start,end+1))
    result,_=compare(full_list,int_list,data_type='list')
    result=list(map(str,result))
    if result!=[] and data_type=='file':
        str_list=list(map(str,int_list))
        save_original(data,str_list)
    elapsed_time=time()-start_time
    return result,elapsed_time
