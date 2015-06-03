#!/usr/bin/python3
# coding:utf-8

from os import getenv
from getpass import getpass

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
    
def file2list(filename,check='on',displayinfo='on'):
    path=getenv('userprofile')+'\\Desktop\\'
    file=open(path+filename)
    data=file.readlines()
    file.close()
    if check.lower()=='on':
        output=precheck(data)
        if output!=data and displayinfo.lower=='on':
            print('Warning, '+filename+'不规范，已经删除空格和回车')
        return output        
    return data

def list2file(l,filename):
    path=getenv('userprofile')+'\\Desktop\\'
    file=open(path+filename,'w')
    for line in l:
        file.write(str(line)+'\n')
    file.close()
    return 0

def menu():
    print('1. Check Repeat(Single File)')
    print('2. File Compare(Two Files)')
    print('Q. Quit')
    return 0

def pause():
    getpass(prompt='Press Enter to continue...')
