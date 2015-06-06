#!/usr/bin/python3
# coding:utf-8

from checkfunction import chk_repeat
from checkfunction import compare
from iolib import menu
from iolib import pause

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
                print('file1.txt has repeated content:')
                print('\n'.join(r1))
                pause()
        elif choice=='2':
            chk_repeat('file1.txt')
            chk_repeat('file2.txt')
            r1=compare('file1.txt','file2.txt')
            r2=compare('file2.txt','file1.txt','off')
            if r1+r2==[]:
                print('file1.txt is same as file2.txt')
                pause()
            elif r1==[]:
                print('file2.txt完全包含file1.txt')
                print('file2.txt比file1.txt多以下内容：')
                print('\n'.join(r2))
            elif r2==[]:
                print('file1.txt完全包含file2.txt')
                print('file1.txt比file2.txt多以下内容：')
                print('\n'.join(r1))
            else:
                print('两个文件互相有缺少内容')
                print('file1.txt比file2.txt多以下内容：')
                print('\n'.join(r1))
                #print('\n')
                print('file2.txt比file1.txt多以下内容：')
                print('\n'.join(r2))
                pause()
        else:
            print('Wrong Choice! Please choose again!')
        menu()
        choice=input()            

if __name__ == '__main__':
    main()

