#!/usr/bin/python3
# coding:utf-8

from lib.comm import precheck
from os import getenv

def file2list(filename,check='on',display_warning='on'):
    path=getenv('userprofile')+'\\Desktop\\'
    file=open(path+filename,encoding='utf-8')
    data=file.readlines()
    file.close()
    data=[i.rstrip('\n') for i in data]     #删除\n
    if check=='on':
        output=precheck(data)
    else:
        output=data
    if display_warning=='on' and output==[]:
        print('[Warning]'+filename+' has no content.')
    return output

def list2file(list_data,filename):
    path=getenv('userprofile')+'\\Desktop\\'
    file=open(path+filename,'w',encoding='utf-8')
    for i in list_data:
        file.write(str(i)+'\n')
    file.close()
    return 0

def save_original(filename,list_data,mode='change'):    #如内容有变，将新文件输出，原文件名加上"_original"
    original_data=file2list(filename,check='off',display_warning='off')
    count=0
    if list_data!=original_data:
        i=filename.rindex('.')
        if mode=='change':
            list2file(list_data,filename)
            list2file(original_data,filename[:i]+'_original'+filename[i:])
            print('[Warning]'+filename+'已经过规范化处理，原文件保存为'+filename[:i]+'_original'+filename[i:])
        else:
            list2file(list_data,filename[:i]+'_new'+filename[i:])
            print(filename+'删除重复内容后，新文件保存为'+filename[:i]+'_new'+filename[i:])
    return 0

def remove_duplicates(filename):
    data=sort_data(list(set(file2list(filename))))
    save_original(filename,data,mode='remove_duplicates')
    return 0
