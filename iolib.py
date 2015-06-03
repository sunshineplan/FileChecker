#!/usr/bin/python3
# coding:utf-8

from os import getenv

def precheck(l):
    count=0
    for line in l:
        line=line.strip('\n')           #删除\n
        line=line.strip()               #删除空格
        l[count]=line
        count+=1
    output=[a for a in l if a!='']      #删除空值
    output.sort()
    return output
    
def file2list(filename,displayinfo='yes'):
    file=open(getenv('userprofile')+'\\Desktop\\'+filename)
    data=file.readlines()
    file.close()
    output=precheck(data)
    if output!=data and displayinfo=='yes':
        print('Warning, '+filename+'不规范，已经删除空格和回车')
    return output

def list2file(l,filename):
    a=precheck(l)
    if a!=l:
        print('Warning, '+filename+'不规范，已经删除空格和回车')
    file=open(getenv('userprofile')+'\\Desktop\\'+filename,'w')
    for line in a:
        file.write(str(line)+'\n')
    file.close()
    return 0
