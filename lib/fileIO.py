#!/usr/bin/python3
# coding:utf-8

from os import getenv, name

from lib.comm import precheck


def file2list(file, check='on', display_warning='on'):
    if name == 'nt':
        path = getenv('userprofile')+'\\Desktop\\'
    else:
        path = getenv('HOME')+'/'
    with open(path+file, encoding='utf-8') as f:
        data = f.readlines()
    data = [i.rstrip('\n') for i in data]  # remove trailing '\n'
    if check == 'on':
        data = precheck(data)
    if display_warning == 'on' and data == []:
        print(f'[Warning]{file} has no content.')
    return data


def list2file(l, file):
    if name == 'nt':
        path = getenv('userprofile')+'\\Desktop\\'
    else:
        path = getenv('HOME')+'/'
    with open(path+file, 'w', encoding='utf-8') as f:
        f.writelines(l)


def save_original(file, l, mode='change'):
    original = file2list(file, check='off', display_warning='off')
    if l == original:
        return
    i = file.rindex('.')
    if mode == 'change':
        list2file(l, file)
        list2file(original, file[:i]+'_original'+file[i:])
        print(
            f'[Warning]{file} has changed after standardization, the original file is saved as {file[:i]}_original{file[i:]}')
    else:
        list2file(l, f'{file[:i]}_new{file[i:]}')
        print(
            f'Duplicates removed, the new file is saved as {file[:i]}_new{file[i:]}')
