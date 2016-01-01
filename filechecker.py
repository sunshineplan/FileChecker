#!/usr/bin/python3
# coding:utf-8

from checkfunction import chk_repeat
from checkfunction import chk_continuity
from checkfunction import compare
from iolib import menu
from iolib import pause
from iolib import printresult

def main():
    print('Welcome to use File Checker')
    menu()
    choice=input('Please choose one function:')
    while choice.lower()!='q':
        if choice=='1':
            r1=chk_repeat('file1.txt')
            if r1==[]:
                print('file1.txt has no repeat')
                pause()
            else:
                title='file1.txt has repeated content:'
                print(title)
                printresult(r1,title)
                pause()
        elif choice=='2':
            chk_repeat('file1.txt')
            chk_repeat('file2.txt')
            r1=compare('file2.txt','file1.txt',chk_have='on')
            if r1==[]:
                print('所需对比的文件完全包含在目标文件内')
                pause()
            else:
                title='所需对比的文件多出以下内容：'
                print(title)
                printresult(r1)
                pause()
        elif choice=='3':
            chk_repeat('file1.txt')
            chk_repeat('file2.txt')
            r1=compare('file1.txt','file2.txt')
            r2=compare('file2.txt','file1.txt','off')
            if r1+r2==[]:
                print('file1.txt is same as file2.txt')
                pause()
            elif r1==[]:
                print('file2.txt完全包含file1.txt')
                title='file2.txt比file1.txt多以下内容：'
                print(title)
                printresult(r2)
            elif r2==[]:
                print('file1.txt完全包含file2.txt')
                title='file1.txt比file2.txt多以下内容：'
                print(title)
                printresult(r1)
            else:
                print('两个文件互相有缺少内容')
                title='file1.txt比file2.txt多以下内容：'
                print(title)
                printresult(r1,title,'1')
                #print('\n')
                title='file2.txt比file1.txt多以下内容：'
                print(title)
                printresult(r2,title,'2')
                pause()
        elif choice=='4':
            r1=chk_continuity('file1.txt')
            if r1==[]:
                print('file1.txt完全是连续的')
                pause()
            else:
                r1=list(map(str,r1))
                title='file1.txt不连续，缺少已下元素：'
                print(title)
                printresult(r1)
                pause()
        else:
            print('Wrong Choice! Please choose again!')
        menu()
        choice=input()            

if __name__ == '__main__':
    main()

