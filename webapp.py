#!/usr/bin/python3
# -*- coding: utf-8 -*-

from flask import Flask, jsonify, render_template, request

from lib.comm import precheck
from lib.func import (chk_consecutive, chk_duplicates, compare,
                      remove_duplicates)
from lib.output import print_result

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/analysis', methods=['POST'])
def sda():
    type = request.form.get('type')
    source = request.form.get('source')
    if source == 'Data1' or source == 'Data2':
        if source == 'Data1':
            data = precheck(str(request.form.get('data1')).split('\n'))
        else:
            data = precheck(str(request.form.get('data2')).split('\n'))
        if data == []:
            return jsonify(result=source + ' is empty.\nPlease enter someting...')
    elif source == 'Data1,Data2':
        data1 = precheck(str(request.form.get('data1')).split('\n'))
        data2 = precheck(str(request.form.get('data2')).split('\n'))
        if data1 == []:
            return jsonify(result='Data1 is empty.\nPlease enter someting...')
        elif data2 == []:
            return jsonify(result='Data2 is empty.\nPlease enter someting...')
    result = []
    if type == 'chk_duplicates':
        r1, elapsed_time = chk_duplicates(data, data_type='list')
        if r1 == []:
            result.append(source + ' contains no duplicate values.\n')
            result.append('Duration for process: ' +
                          str(round(elapsed_time, 3)) + ' sec.')
        else:
            result += print_result(
                r1,
                title1='Duplicate values found in ' + source,
                elapsed_time=elapsed_time,
                result2file='off',
                display='off')
    elif type == 'rm_duplicates':
        result = remove_duplicates(data, data_type='list')
    elif type == 'chk_consecutive':
        try:
            r1, elapsed_time1 = chk_consecutive(data, data_type='list')
            tmp, elapsed_time2 = chk_duplicates(data, data_type='list')
            elapsed_time = elapsed_time1 + elapsed_time2
        except ValueError:
            result.append(
                '[Error]' + source +
                ' contains non-numeric value. Please check and try again!'
            )
        else:
            if tmp != []:
                result.append(
                    '[Warning]Duplicate values found in ' + source +
                    '.\nYou can "Check Duplicates (' +
                    source + ')" to check it.\n'
                )
            if r1 == []:
                result.append(
                    source + ' contains consecutive natural numbers.\n')
                result.append('Duration for process: ' +
                              str(round(elapsed_time, 3)) + ' sec.')
            else:
                result += print_result(
                    r1,
                    title1=source + ' is not consecutive',
                    title2='The following numbers are missing:',
                    elapsed_time=elapsed_time,
                    result2file='off',
                    display='off')
    elif type == 'compare':
        mode = request.form.get('mode')
        ignore_duplicates = request.form.get('ignore_duplicates')
        if ignore_duplicates == 'true':
            data1 = remove_duplicates(data1, data_type='list')
            data2 = remove_duplicates(data2, data_type='list')
        if mode == 'comm':
            r1, elapsed_time = compare(
                data1, data2, mode='comm', data_type='list')
            if r1 == []:
                result.append('Two data contain no common values.\n')
                result.append('Duration for process: ' +
                              str(round(elapsed_time, 3)) + ' sec.')
            else:
                result += print_result(
                    r1,
                    title1='Common values found between two data.',
                    elapsed_time=elapsed_time,
                    result2file='off',
                    display='off')
        elif mode == 'diff':
            r1, elapsed_time1 = compare(data1, data2, data_type='list')
            r2, elapsed_time2 = compare(data2, data1, data_type='list')
            elapsed_time = elapsed_time1 + elapsed_time2
            if r1 + r2 == []:
                result.append('Data1 is same as Data2.\n')
                result.append('Duration for process: ' +
                              str(round(elapsed_time, 3)) + ' sec.')
            elif r1 == []:
                result.append('Data2 completely contains Data1.\n')
                result += print_result(
                    r2,
                    title1='Data2 is more than Data1',
                    elapsed_time=elapsed_time,
                    result2file='off',
                    display='off')
            elif r2 == []:
                result.append('Data1 completely contains Data2.\n')
                result += print_result(
                    r1,
                    title1='Data1 is more than Data2',
                    elapsed_time=elapsed_time,
                    result2file='off',
                    display='off')
            else:
                result.append('Two files have inconsistent content.\n')
                result += print_result(
                    r1, title1='Data1 is more than Data2', result2file='off', display='off')
                result.append('')
                result += print_result(
                    r2,
                    title1='Data2 is more than Data1',
                    elapsed_time=elapsed_time,
                    result2file='off',
                    display='off')
    output = '\n'.join(result)
    return jsonify(result=output)


if __name__ == '__main__':
    app.run()
