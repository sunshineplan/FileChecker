#!/usr/bin/python3

from difflib import unified_diff
from time import time

from util import precheck, sort


def chk_duplicates(data):
    start_time = time()
    result = []
    tmp = ''
    data = precheck(data)
    for i in data.copy():
        if i == tmp:
            data.remove(i)
            continue
        if data.count(i) != 1:
            result.append(f'{i}\t\tappears {data.count(i)} time(s)')
        tmp = i
        data.remove(i)
    result = sort(result)
    return result, time()-start_time


def compare(data1, data2, mode='diff'):
    start_time = time()
    data1 = precheck(data1)
    data2 = precheck(data2)
    result = []
    if mode == 'diff':
        result = data1.copy()
        for i in data2:
            if i in result:
                result.remove(i)
    else:
        data2 = list(set(data2))
        for i in data2:
            if data1.count(i) != 0:
                result.append(i)
    result = sort(result)
    return result, time()-start_time


def chk_consecutive(data):
    start_time = time()
    data = precheck(data)
    data = sorted(list(map(int, data)))
    full = list(range(data[0], data[-1]+1))
    result, _ = compare(full, data)
    result = list(map(str, result))
    return result, time()-start_time


def diff(data1, data2):
    return unified_diff(data1, data2, fromfile='Data1', tofile='Data2')
