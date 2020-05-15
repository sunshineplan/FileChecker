#!/usr/bin/python3

from difflib import unified_diff

from util import precheck, sort


def chk_duplicates(data):
    result = []
    tmp = ''
    data = precheck(data)
    for i in data.copy():
        if i == tmp:
            data.remove(i)
            continue
        if data.count(i) != 1:
            result.append((i, data.count(i)))
        tmp = i
        data.remove(i)
    result.sort(reverse=True, key=lambda i: i[1])
    return result


def compare(data1, data2, mode='diff'):
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
    return result


def chk_consecutive(data):
    data = precheck(data)
    data = sorted(list(map(int, data)))
    full = list(range(data[0], data[-1]+1))
    result = compare(full, data)
    return result


def diff(data1, data2):
    return unified_diff(data1, data2, fromfile='Data1', tofile='Data2')
