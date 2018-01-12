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
    output=sortdata(output)
    return output
    
def file2list(filename,check='on',displayinfo='on',removeduplicate='off'):
    path=getenv('userprofile')+'\\Desktop\\'
    file=open(path+filename,encoding='utf-8')
    data=file.readlines()
    file.close()
    if check=='on':
        output=precheck(data)
        if output!=data and displayinfo=='on':
            print('Warning, '+filename+'不规范，已经删除空格和回车')
        data=output
    if removeduplicate='on':
        data=list(set(data))            #删除重复值
    return data

def list2file(l,filename):
    path=getenv('userprofile')+'\\Desktop\\'
    file=open(path+filename,'w',encoding='utf-8')
    for line in l:
        file.write(str(line)+'\n')
    file.close()
    return 0

def menu():
    print('1. Check Repeat(Single File)')
    print('2. Check Have(Two Files)')
    print('3. File Compare(Two Files)')
    print('4. Check Continuity(Single File)')
    print('Q. Quit')
    return 0

def pause():
    getpass(prompt='Press Enter to continue...')

def sortdata(data):
    #r=sorted(data, key=lambda item:(int(item.partition(' ')[0]) if item[0].isdigit() else float('inf'), item))
    r=sorted(data)
    return r

def saveoriginal(filename,l):
    originalfile=file2list(filename,'off')
    for line in originalfile:
        line=line.strip('\n')
        originalfile[count]=line
        count+=1
    if l!=originalfile:
        i=filename.rindex('.')
        changed=list(set(l))
        changed=sortdata(changed)
        list2file(originalfile,filename[:i]+'_original'+filename[i:])
        list2file(changed,filename)
        print(filename+'文件已经过规范化处理，原文件保存为'+filename[:i]+'_original'+filename[i:])
    return 0    

def printresult(r,title='result:',ext=''):
    filename='result'+ext+'.txt'
    if len(r)>17:
        r.insert(0,title)
        list2file(r,filename)
        print('由于结果太大，已将其输出到'+filename)
    else:
        print('\n'.join(r))
    return 0
