#!/usr/bin/python3
# coding:utf-8

from lib.fn import chk_duplicates
from lib.fn import compare
from lib.fn import chk_consecutive
from lib.comm import print_result
from lib.io import remove_duplicates
from os import system
from os import name
from getpass import getpass

def menu():
    print('   * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *')
    print('   *                                                           *')
    print('   *  Welcome to use File Checker!                             *')
    print('   *                                                           *')
    print('   *  1. Check Duplicates (File1)                              *')
    print('   *  2. Cross Compare (Common)                                *')
    print('   *  3. Cross Compare (Difference)                            *')
    print('   *  4. Check Consecutive (File1) (Numeric Value Only)        *')
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

def main():
    while True:
        choice=menu()
        if choice=='1':
            try:
                r1,elapsed_time=chk_duplicates('file1.txt')
            except FileNotFoundError:
                print('[Error]file1.txt not found. Please put file1.txt on the Desktop.')
                pause()
            else:
                if r1==[]:
                    print('file1.txt contains no duplicate values.\n')
                    print('Duration for process: '+str(round(elapsed_time,3))+' sec.')
                    pause()
                else:
                    print_result(r1,title1='Duplicate values found in file1.txt',elapsed_time=elapsed_time)
                    choice=input('Do you want to remove duplicate values (yes/no)?')
                    while True:
                        if choice.lower()=='yes':
                            remove_duplicates('file1.txt')
                            break
                        elif choice.lower()=='no':
                            break
                        else:
                            choice=input("Please type 'yes' or 'no':")
                    pause()
        elif choice=='2':
            try:
                r1,elapsed_time=compare('file1.txt','file2.txt',mode='comm')
            except FileNotFoundError:
                print('[Error]file1.txt or file2.txt not found. Please put this files on the Desktop.')
                pause()
            else:
                if r1==[]:
                    print('Two files contain no common values.\n')
                    print('Duration for process: '+str(round(elapsed_time,3))+' sec.')
                    pause()
                else:
                    print_result(r1,title1='Common values found between two files',elapsed_time=elapsed_time)
                    pause()
        elif choice=='3':
            try:
                r1,elapsed_time1=compare('file1.txt','file2.txt')
                r2,elapsed_time2=compare('file2.txt','file1.txt',display_warning='off')
                elapsed_time=elapsed_time1+elapsed_time2
            except FileNotFoundError:
                print('[Error]file1.txt or file2.txt not found. Please put this files on the Desktop.')
                pause()
            else:
                if r1+r2==[]:
                    print('file1.txt is same as file2.txt.\n')
                    print('Duration for process: '+str(round(elapsed_time,3))+' sec.')
                    pause()
                elif r1==[]:
                    print('file2.txt完全包含file1.txt。\n')
                    print_result(r2,title1='file2.txt比file1.txt多以下内容',elapsed_time=elapsed_time)
                    pause()
                elif r2==[]:
                    print('file1.txt完全包含file2.txt。\n')
                    print_result(r1,title1='file1.txt比file2.txt多以下内容',elapsed_time=elapsed_time)
                    pause()
                else:
                    print('两个文件有互相不一致内容\n')
                    print_result(r1,title1='file1.txt比file2.txt多以下内容',ext='1')
                    print()
                    print_result(r2,title1='file2.txt比file1.txt多以下内容',ext='2',elapsed_time=elapsed_time)
                    pause()
        elif choice=='4':
            try:
                r1,elapsed_time1=chk_consecutive('file1.txt')
                tmp,elapsed_time2=chk_duplicates('file1.txt',display_warning='off')
                elapsed_time=elapsed_time1+elapsed_time2
            except FileNotFoundError:
                print('[Error]file1.txt not found. Please put file1.txt on the Desktop.')
                pause()
            except ValueError:
                print('[Error]file1.txt contains non-numeric value. Please check and try again!')
                pause()
            else:
                if tmp!=[]:
                    print('[Warning]Duplicate values found in file1.txt, you can check duplicates later.')
                if r1==[]:
                    print('file1.txt contains consecutive number.')
                    print('\nDuration for process: '+str(round(elapsed_time,3))+' sec.')
                    pause()
                else:
                    print_result(r1,title1='file1.txt不连续',title2='缺少以下元素：',elapsed_time=elapsed_time)
                    pause()
        elif choice.lower()=='q':
            break
        else:
            pause(mode='error')
    return 0

if __name__ == '__main__':
    main()
