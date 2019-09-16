#!/usr/bin/python3
# coding:utf-8

from os import name, system

from lib.func import (chk_consecutive, chk_duplicates, compare,
                      remove_duplicates)
from lib.output import print_result


def menu():
    print('   * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *')
    print('   *                                                           *')
    print('   *  Welcome to use Simple Data Analysis!                     *')
    print('   *                                                           *')
    print('   *  1. Check Duplicates (File1)                              *')
    print('   *  2. Cross Compare (Common)                                *')
    print('   *  3. Cross Compare (Difference)                            *')
    print('   *  4. Check Consecutive (File1) (Numeric Value Only)        *')
    print('   *  Q. Quit                                                  *')
    print('   *                                                           *')
    print('   * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *')
    print()
    choice = input('Please choose one function:')
    print()
    return choice


def pause(mode='normal'):
    print()
    if mode == 'normal':
        prompt = 'Press any key to continue...'
    else:
        prompt = 'Wrong choice! Press any key to choose again!'
    system('echo '+prompt+'&pause>nul' if name ==
           'nt' else '/bin/bash -c "read -n1 -sp \''+prompt+'\'"')
    system('cls' if name == 'nt' else 'clear')


def main():
    while True:
        choice = menu()
        if choice == '1':
            try:
                r1, elapsed_time = chk_duplicates('file1.txt')
            except FileNotFoundError:
                print(
                    '[Error]file1.txt not found. Please put file1.txt on your Desktop(Windows) or Home directory(Linux).')
                pause()
            else:
                if r1 == []:
                    print('file1.txt contains no duplicate values.\n')
                    print('Duration for process: ' +
                          str(round(elapsed_time, 3))+' sec.')
                    pause()
                else:
                    print_result(
                        r1, title1='Duplicate values found in file1.txt.', elapsed_time=elapsed_time)
                    choice = input(
                        'Do you want to remove duplicate values (yes/no)?')
                    while True:
                        if choice.lower() == 'yes':
                            remove_duplicates('file1.txt')
                            break
                        elif choice.lower() == 'no':
                            break
                        else:
                            choice = input("Please type 'yes' or 'no':")
                    pause()
        elif choice == '2':
            try:
                r1, elapsed_time = compare(
                    'file1.txt', 'file2.txt', mode='comm')
            except FileNotFoundError:
                print(
                    '[Error]file1.txt or file2.txt not found. Please put this files on your Desktop(Windows) or Home directory(Linux).')
                pause()
            else:
                if r1 == []:
                    print('Two files contain no common values.\n')
                    print('Duration for process: ' +
                          str(round(elapsed_time, 3))+' sec.')
                    pause()
                else:
                    print_result(
                        r1, title1='Common values found between two files.', elapsed_time=elapsed_time)
                    pause()
        elif choice == '3':
            try:
                r1, elapsed_time1 = compare('file1.txt', 'file2.txt')
                r2, elapsed_time2 = compare(
                    'file2.txt', 'file1.txt', display_warning='off')
                elapsed_time = elapsed_time1+elapsed_time2
            except FileNotFoundError:
                print(
                    '[Error]file1.txt or file2.txt not found. Please put this files on your Desktop(Windows) or Home directory(Linux).')
                pause()
            else:
                if r1+r2 == []:
                    print('file1.txt is same as file2.txt.\n')
                    print('Duration for process: ' +
                          str(round(elapsed_time, 3))+' sec.')
                    pause()
                elif r1 == []:
                    print('file2.txt completely contains file1.txt。\n')
                    print_result(
                        r2, title1='file2.txt is more than file1.txt', elapsed_time=elapsed_time)
                    pause()
                elif r2 == []:
                    print('file1.txt completely contains file2.txt。\n')
                    print_result(
                        r1, title1='file1.txt is more than file2.txt', elapsed_time=elapsed_time)
                    pause()
                else:
                    print('Two files have inconsistent content.\n')
                    print_result(
                        r1, title1='file1.txt is more than file2.txt', ext='1')
                    print()
                    print_result(r2, title1='file2.txt is more than file1.txt',
                                 ext='2', elapsed_time=elapsed_time)
                    pause()
        elif choice == '4':
            try:
                r1, elapsed_time1 = chk_consecutive('file1.txt')
                tmp, elapsed_time2 = chk_duplicates(
                    'file1.txt', display_warning='off')
                elapsed_time = elapsed_time1+elapsed_time2
            except FileNotFoundError:
                print(
                    '[Error]file1.txt not found. Please put file1.txt on the Desktop.')
                pause()
            except ValueError:
                print(
                    '[Error]file1.txt contains non-numeric value. Please check and try again!')
                pause()
            else:
                if tmp != []:
                    print(
                        '[Warning]Duplicate values found in file1.txt, you can check duplicates later.\n')
                if r1 == []:
                    print('file1.txt contains consecutive natural numbers.\n')
                    print('Duration for process: ' +
                          str(round(elapsed_time, 3))+' sec.')
                    pause()
                else:
                    print_result(r1, title1='file1.txt is not consecutive',
                                 title2='The following numbers are missing:', elapsed_time=elapsed_time)
                    pause()
        elif choice.lower() == 'q':
            break
        else:
            pause(mode='error')


if __name__ == '__main__':
    main()
