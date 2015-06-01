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
        if choice=='1':
            result=chk_repeat('file1.txt')
            if result==[]:
                print('file1.txt has no repeat')
                pause()
            else:
                print('file1.txt has repeated content:')
                print('\n'.join(result))
                pause()
        elif choice=='2':
            result=compare('file1.txt','file2.txt')
            if result==[]:
                print('file1.txt is same as file2.txt')
                pause()
            else:
                print('file2.txt missing some contents')
                print('\n'.join(result))
                pause()
        else:
            print('Wrong Choice! Please choose again!')
        menu()
        choice=input()            

if __name__ == '__main__':
    main()

