#!/usr/bin/python3
# coding:utf-8

from os import getenv, name

from lib.comm import precheck, sort_data


def file2list(filename, check='on', display_warning='on'):
    if name == 'nt':
        path = getenv('userprofile')+'\\Desktop\\'
    else:
        path = getenv('HOME')+'/'
    file = open(path+filename, encoding='utf-8')
    data = file.readlines()
    file.close()
    data = [i.rstrip('\n') for i in data]  # remove trailing '\n'
    if check == 'on':
        output = precheck(data)
    else:
        output = data
    if display_warning == 'on' and output == []:
        print('[Warning]'+filename+' has no content.')
    return output


def list2file(list_data, filename):
    if name == 'nt':
        path = getenv('userprofile')+'\\Desktop\\'
    else:
        path = getenv('HOME')+'/'
    file = open(path+filename, 'w', encoding='utf-8')
    for i in list_data:
        file.write(str(i)+'\n')
    file.close()


def save_original(filename, list_data, mode='change'):
    original_data = file2list(filename, check='off', display_warning='off')
    if list_data != original_data:
        i = filename.rindex('.')
        if mode == 'change':
            list2file(list_data, filename)
            list2file(original_data, filename[:i]+'_original'+filename[i:])
            print('[Warning]'+filename+' has changed after standardization, the original file is saved as ' +
                  filename[:i]+'_original'+filename[i:])
        else:
            list2file(list_data, filename[:i]+'_new'+filename[i:])
            print('Duplicates removed, the new file is saved as ' +
                  filename[:i]+'_new'+filename[i:])
