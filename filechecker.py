#!/usr/bin/python3
# coding:utf-8

from checkfunction import chk_repeat
from checkfunction import chk_consecutive
from checkfunction import compare
from iolib import menu
from iolib import pause
from iolib import print_result

def main():
    while True:
        choice=menu()
        if choice=='1':
            try:
                r1=chk_repeat('file1.txt')
            except FileNotFoundError:
                print('file1.txt not found. Please put file1.txt on the Desktop.')
                pause()
            else:
                if r1==[]:
                    print('file1.txt has no repeated contents.')
                    pause()
                else:
                    print_result(r1,title1='file1.txt has repeated content(s)')
                    pause()
        elif choice=='2':
            try:
                r1=chk_repeat('file1.txt','file2.txt')
            except FileNotFoundError:
                print('file1.txt or file2.txt not found. Please put this files on the Desktop.')
                pause()
            else:
                if r1==[]:
                    print('Two files have no repeated contents.')
                    pause()
                else:
                    print_result(r1,title1='Two files have repeated content(s)')
                    pause()
        elif choice=='3':
            try:
                r1=compare('file1.txt','file2.txt')
                r2=compare('file2.txt','file1.txt',display_warning='off')
            except FileNotFoundError:
                print('file1.txt or file2.txt not found. Please put this files on the Desktop.')
                pause()
            else:
                if r1+r2==[]:
                    print('file1.txt is same as file2.txt.')
                    pause()
                elif r1==[]:
                    print('file2.txt完全包含file1.txt。')
                    print_result(r2,title1='file2.txt比file1.txt多以下内容')
                    pause()
                elif r2==[]:
                    print('file1.txt完全包含file2.txt。')
                    print_result(r1,title1='file1.txt比file2.txt多以下内容')
                    pause()
                else:
                    print('两个文件互相有缺少内容')
                    print_result(r1,title1='file1.txt比file2.txt多以下内容',ext='1')
                    print_result(r2,title1='file2.txt比file1.txt多以下内容',ext='2')
                    pause()
        elif choice=='4':
            try:
                r1=chk_consecutive('file1.txt')
            except FileNotFoundError:
                print('file1.txt not found. Please put file1.txt on the Desktop.')
                pause()
            else:
                if r1==[]:
                    print('file1.txt contains consecutive number.')
                    pause()
                else:
                    print_result(r1,title1='file1.txt不连续',title2='缺少以下元素：')
                    pause()
        elif choice.lower()=='q':
            break
        else:
            pause(mode='error')

if __name__ == '__main__':
    main()

