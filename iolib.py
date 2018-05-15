#!/usr/bin/python3
# coding:utf-8

from os import getenv
from os import system
from os import name
from getpass import getpass

def precheck(list_data):
    data=[i.strip() for i in list_data]     #删除空格
    data=[i for i in data if i!='']         #删除空值
    output=sort_data(data)
    return output
    
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

def menu():
    print('   * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *')
    print('   *                                                           *')
    print('   *  Welcome to use File Checker!                             *')
    print('   *                                                           *')
    print('   *  1. Check Repeat(Single File)                             *')
    print('   *  2. Check Repeat(Two Files)                               *')
    print('   *  3. File Compare(Two Files)                               *')
    print('   *  4. Check Consecutive(Single File)(Numeric Content Only)  *')
    print('   *  Q. Quit                                                  *')
    print('   *                                                           *')
    print('   * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *')
    print()
    choice=input('Please choose one function:')
    print()
    return choice

def pause(mode='normal'):
    print()
    if mode=='normal':
        getpass(prompt='Press Enter to continue...')
    else:
        getpass(prompt='Wrong choice! Please choose again!')
    system('cls' if name=='nt' else 'clear')
    return 0

def sort_data(list_data):
    #output=sorted(list_data, key=lambda item:(int(item.partition(' ')[0]) if item[0].isdigit() else float('inf'), item))
    output=sorted(list_data)
    return output

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

def remove_repeat(filename):
    data=sort_data(list(set(file2list(filename))))
    save_original(filename,data,mode='remove_repeat')
    return 0

def print_result(result,title1='',title2='result:',ext='',elapsed_time=-1,result2file='on',display='on'):
    content=[]
    record=len(result)
    content.append(title1)
    content.append('\nTotal '+str(record)+' record(s)\n')
    content.append(title2)
    filename='result'+ext+'.txt'
    if record>17 and result2file=='on':
        list2file(content+result,filename)
        content.append('由于结果太大，已将其输出到'+filename)
    else:
        content=content+result
    if elapsed_time>=0:
        content.append('\n本次处理耗时'+str(round(elapsed_time,3))+'秒')
    if display=='on':
        print('\n'.join(content))
        return 0
    return content
