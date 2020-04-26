#!/usr/bin/python3
# coding:utf-8

from lib.fileIO import list2file


def print_result(result, title1='', title2='result:', ext='', elapsed_time=-1, result2file='on', display='on'):
    content = []
    content.append(title1)
    content.append(f'\nTotal {len(result)} record(s)\n')
    content.append(title2)
    file = f'result{ext}.txt'
    if len(result) > 17 and result2file == 'on':
        list2file(content+result, file)
        content.append(
            f'Since the result is too large, it has been output to {file}')
    else:
        content += result
    if elapsed_time >= 0:
        content.append(
            f'\nDuration for process: {str(round(elapsed_time, 3))} sec.')
    if display == 'on':
        print('\n'.join(content))
        return
    return content
