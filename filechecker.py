#!/usr/bin/python3
# coding:utf-8

from checkfunction import chk_repeat#chk_repeat(filename) return list which is repeated with repeated times
from checkfunction import compare#compare(file1,file2) return which is file1 larger than file2
from getpass import getpass

def menu():
    print('1. Check Repeat(Single File)')
    print('2. File Compare(Two Files)')
    print('Q. Quit')
    return 0

def pause():
    getpass(prompt='Press Enter to continue...')

def main():
    print('Welcome to use File Checker')
    menu()
    choice=input('Please choose one function:')
    while choice.lower()!='q':
        r1=[]
        r2=[]
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
            r1=compare('file1.txt','file2.txt')
            r2=compare('file2.txt','file1.txt')
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
                print('\n')
                print('file2.txt比file1.txt多以下内容：')
                print('\n'.join(r2))
                pause()
        else:
            print('Wrong Choice! Please choose again!')
        menu()
        choice=input()            

if __name__ == '__main__':
    main()

