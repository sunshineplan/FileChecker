#!/usr/bin/python3
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, jsonify
from lib.func import chk_duplicates
from lib.func import remove_duplicates
from lib.func import compare
from lib.func import chk_consecutive
from lib.comm import precheck
from lib.output import print_result

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/analysis', methods=['POST'])
def sda():
    type = request.form.get('type')
    source = request.form.get('source')
    data1 = precheck(str(request.form.get('data1')).split('\n'))
    data2 = precheck(str(request.form.get('data2')).split('\n'))
    result = []
    if data1 == []:
        if source == 'Data1' or source == 'Data1,Data2':
            return jsonify(result='Data1 is empty.\nPlease enter someting...')
    elif data2 == []:
        if source == 'Data2' or source == 'Data1,Data2':
            return jsonify(result='Data2 is empty.\nPlease enter someting...')
    if type == 'chk_duplicates':
        r1, elapsed_time = chk_duplicates(data1, data_type='list')
        if r1 == []:
            result.append('Data1 contains no duplicate values.\n')
            result.append('Duration for process: ' +
                          str(round(elapsed_time, 3)) + ' sec.')
        else:
            result += print_result(
                r1,
                title1='Duplicate values found in Data1.',
                elapsed_time=elapsed_time,
                result2file='off',
                display='off')
    elif type == 'rm_duplicates':
        if source == 'Data1' and data1 != []:
            result = remove_duplicates(data1, data_type='list')
        elif source == 'Data2' and data2 != []:
            result = remove_duplicates(data2, data_type='list')
    elif type == 'chk_comm':
        r1, elapsed_time = compare(data1, data2, mode='comm', data_type='list')
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
    elif type == 'chk_diff':
        r1, elapsed_time1 = compare(data1, data2, data_type='list')
        r2, elapsed_time2 = compare(data2, data1, data_type='list')
        elapsed_time = elapsed_time1 + elapsed_time2
        if r1 + r2 == []:
            result.append('Data1 is same as Data2.\n')
            result.append('Duration for process: ' +
                          str(round(elapsed_time, 3)) + ' sec.')
        elif r1 == []:
            result.append('Data2完全包含Data1。\n')
            result += print_result(
                r2,
                title1='Data2比Data1多以下内容',
                elapsed_time=elapsed_time,
                result2file='off',
                display='off')
        elif r2 == []:
            result.append('Data1完全包含Data2。\n')
            result += print_result(
                r1,
                title1='Data1比Data2多以下内容',
                elapsed_time=elapsed_time,
                result2file='off',
                display='off')
        else:
            result.append('两个数据有互相不一致内容。\n')
            result += print_result(
                r1, title1='Data1比Data2多以下内容', result2file='off', display='off')
            result.append('')
            result += print_result(
                r2,
                title1='Data2比Data1多以下内容',
                elapsed_time=elapsed_time,
                result2file='off',
                display='off')
    elif type == 'chk_consecutive':
        try:
            r1, elapsed_time1 = chk_consecutive(data1, data_type='list')
            tmp, elapsed_time2 = chk_duplicates(data1, data_type='list')
            elapsed_time = elapsed_time1 + elapsed_time2
        except ValueError:
            result.append(
                '[Error]Data1 contains non-numeric value. Please check and try again!'
            )
        else:
            if tmp != []:
                result.append(
                    '[Warning]Duplicate values found in Data1.\nYou can "Check Duplicates (Data1)" to check it.\n'
                )
            if r1 == []:
                result.append('Data1 contains consecutive natural numbers.\n')
                result.append('Duration for process: ' +
                              str(round(elapsed_time, 3)) + ' sec.')
            else:
                result += print_result(
                    r1,
                    title1='Data1不连续',
                    title2='缺少以下元素：',
                    elapsed_time=elapsed_time,
                    result2file='off',
                    display='off')
    output = '\n'.join(result)
    return jsonify(result=output)


if __name__ == '__main__':
    app.run()
