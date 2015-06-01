#!/usr/bin/python3
# coding:utf-8

from checkfunction import chk_repeat#chk_repeat(filename) return list which is repeated with repeated times
from checkfunction import compare#compare(file1,file2) return which is file1 larger than file2
from iolib import printlist

def menu():
    print('1. Check Repeat(Single File)')
    print('2. File Compare(Two Files)')
    print('Q. Quit')
    return 0

def main():
    print('File Checker')
    menu()
    choice=''
    while choice.lower()!='q':
        choice=input('Please choose one function:')
        if choice=='1':
            result=chk_repeat('file1.txt')
            if result==[]:
                print('file1.txt has no repeat')
            else:
                print('file1.txt has repeated content:')
                print(result)
                printlist(result)
        elif choice=='2':
            result=compare('file1.txt','file2.txt')
            if result==[]:
                print('file1.txt is same as file2.txt')
            else:
                print('file2.txt missing some contents')
                printlist(result)
        else:
            print('Wrong Choice! Please choose again!')
            menu()
            choice=input()            

if __name__ == '__main__':
    main()

