#!/usr/bin/python3
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, jsonify
from lib.fn import chk_duplicates
from lib.fn import compare
from lib.fn import chk_consecutive
from lib.comm import print_result
from lib.comm import precheck

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/check', methods=['POST'])
def filechecker():
    type = request.form.get('type')
    data1 = request.form.get('data1')
    data2 = request.form.get('data2')
    data1 = precheck(str(data1).split('\n'))
    data2 = precheck(str(data2).split('\n'))
    result = []
    if data1 == []:
        return jsonify(result='Data1 is empty.\nPlease enter someting...')
    if type == 'chk_duplicates':
        r1, elapsed_time = chk_duplicates(data1, data_type='list')
        if r1 == []:
            result.append('Data1 contains no duplicate values.\n')
            result.append('Duration for process: ' +
                          str(round(elapsed_time, 3)) + ' sec.')
        else:
            result += print_result(
                r1,
                title1='Duplicate values found in Data1',
                elapsed_time=elapsed_time,
                result2file='off',
                display='off')
    elif type == 'chk_comm':
        if data2 == []:
            return jsonify(result='Data2 is empty.\nPlease enter someting...')
        r1, elapsed_time = compare(data1, data2, mode='comm', data_type='list')
        if r1 == []:
            result.append('Two data contain no common values.\n')
            result.append('Duration for process: ' +
                          str(round(elapsed_time, 3)) + ' sec.')
        else:
            result += print_result(
                r1,
                title1='Common values found between two data',
                elapsed_time=elapsed_time,
                result2file='off',
                display='off')
    elif type == 'chk_diff':
        if data2 == []:
            return jsonify(result='Data2 is empty.\nPlease enter someting...')
        r1, elapsed_time1 = compare(data1, data2, data_type='list')
        r2, elapsed_time2 = compare(
            data2, data1, display_warning='off', data_type='list')
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
            result.append('两个数据有互相不一致内容\n')
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
            tmp, elapsed_time2 = chk_duplicates(
                data1, display_warning='off', data_type='list')
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
                result.append('Data1 contains consecutive number.\n')
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
