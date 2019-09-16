#!/usr/bin/python3
# coding:utf-8

from time import time

from lib.comm import precheck, sort_data
from lib.fileIO import file2list, save_original


def chk_duplicates(data, data_type='file', display_warning='on'):
    start_time = time()
    result = []
    tmp = ''
    if data_type == 'file':
        _list = file2list(data)
        if display_warning == 'on':
            save_original(data, _list)
    else:
        _list = precheck(data)
    for i in _list.copy():
        if i == tmp:
            _list.remove(i)
            continue
        if _list.count(i) != 1:
            result.append(str(i)+'\t\tappears '+str(_list.count(i))+' time(s)')
        tmp = i
        _list.remove(i)
    result = sort_data(result)
    elapsed_time = time()-start_time
    return result, elapsed_time


def compare(data1, data2, data_type='file', mode='diff', display_warning='on'):
    start_time = time()
    result = []
    if data_type == 'file':
        if display_warning == 'on':
            list1 = file2list(data1)
            list2 = file2list(data2)
            save_original(data1, list1)
            save_original(data2, list2)
        else:
            list1 = file2list(data1, display_warning='off')
            list2 = file2list(data2, display_warning='off')
    else:
        list1 = data1
        list2 = data2
    if mode == 'diff':
        result = list1.copy()
        for i in list2:
            if i in result:
                result.remove(i)
    else:
        list2 = list(set(list2))
        for i in list2:
            if list1.count(i) != 0:
                result.append(i)
    result = sort_data(result)
    elapsed_time = time()-start_time
    return result, elapsed_time


def chk_consecutive(data, data_type='file'):
    start_time = time()
    if data_type == 'file':
        list_data = file2list(data)
    else:
        list_data = data
    # Convert all strings in a list to int
    int_list = sorted(list(map(int, list_data)))
    start = int_list[0]
    end = int_list[-1]
    full_list = list(range(start, end+1))
    result, _ = compare(full_list, int_list, data_type='list')
    result = list(map(str, result))
    if result != [] and data_type == 'file':
        str_list = list(map(str, int_list))
        save_original(data, str_list)
    elapsed_time = time()-start_time
    return result, elapsed_time


def remove_duplicates(data, data_type='file'):
    if data_type == 'file':
        list_data = file2list(data)
    else:
        list_data = data
    list_data = sort_data(list(set(list_data)))
    if data_type == 'file':
        save_original(data, list_data, mode='remove_duplicates')
    return list_data
