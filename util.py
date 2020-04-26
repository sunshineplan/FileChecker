#!/usr/bin/python3
# coding:utf-8

from re import match


def precheck(l):
    output = [i.strip() for i in l]
    output = [i for i in output if i != '']
    return sort(output)


def sort(l):
    return sorted(l, key=lambda i: (int(match(r'^\d+', i).group(0)) if match(r'^\d+', i) else float('inf'), i))


def print_result(result, title1='', title2='result:', ext='', elapsed_time=-1):
    content = []
    content.append(title1)
    content.append(f'\nTotal {len(result)} record(s)\n')
    content.append(title2)
    content += result
    if elapsed_time >= 0:
        content.append(
            f'\nDuration for process: {elapsed_time:.3f} sec.')
    return content
