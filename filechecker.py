#!/usr/bin/python3

from iolib import file2list
from iolib import list2file
from checkfunction import chk_repeat
from checkfunction import compare

a=file2list('file1.txt')
b=file2list('file2.txt')
c=compare(a,b)
print('结果相差',len(c),'条记录')
list2file(c,'output.txt')


