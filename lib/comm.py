#!/usr/bin/python3
# coding:utf-8

from re import match


def precheck(l):
    output = [i.strip() for i in l]  # remove backspace
    output = [i for i in output if i != '']  # remove empty string
    return sort(output)


def sort(l):
    return sorted(l, key=lambda i: (int(match(r'^\d+', i).group(0)) if match(r'^\d+', i) else float('inf'), i))
