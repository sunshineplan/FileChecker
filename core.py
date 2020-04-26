#!/usr/bin/python3

from time import time

from util import precheck, sort


def chk_duplicates(data):
    start_time = time()
    result = []
    tmp = ''
    l = precheck(data)
    for i in l.copy():
        if i == tmp:
            l.remove(i)
            continue
        if l.count(i) != 1:
            result.append(f'{i}\t\tappears {l.count(i)} time(s)')
        tmp = i
        l.remove(i)
    result = sort(result)
    return result, time()-start_time


def compare(data1, data2, mode='diff'):
    start_time = time()
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
    l = sorted(list(map(int, data)))
    full = list(range(l[0], l[-1]+1))
    result, _ = compare(full, l)
    result = list(map(str, result))
    return result, time()-start_time
