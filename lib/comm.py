#!/usr/bin/python3
# coding:utf-8

from re import match


def precheck(list_data):
    data = [i.strip() for i in list_data]  # remove backspace
    data = [i for i in data if i != '']  # remove empty string
    output = sort_data(data)
    return output


def sort_data(list_data):
    return sorted(list_data, key=lambda i: (int(match(r'^\d+', i).group(0)) if match(r'^\d+', i) else float('inf'), i))
