#!/usr/bin/python3
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, jsonify
from checkfunction import chk_repeat
from checkfunction import chk_consecutive
from checkfunction import compare
from iolib import print_result
from iolib import precheck

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/check', methods=['POST'])
def filechecker():
    type = request.form.get('type')
    file1 = request.form.get('file1')
    file2 = request.form.get('file2')
    data1 = precheck(str(file1).split('\n'))
    data2 = precheck(str(file2).split('\n'))
    result = []
    if data1 == []:
        result.append('File1 was empty.\nPlease enter someting...')
        return jsonify(result=result)
    if type == 'chk_repeat_1':
        r1, elapsed_time = chk_repeat(data1, data_type='list')
        if r1 == []:
            result.append('File1 has no repeated contents.\n')
            result.append('Duration for process: ' +
                          str(round(elapsed_time, 3)) + ' sec.')
        else:
            result.append(
                print_result(
                    r1,
                    title1='File1 has repeated content(s)',
                    elapsed_time=elapsed_time,
                    result2file='off',
                    display='off'))
    elif type == 'chk_repeat_2':
        if data2 == []:
            result.append('File2 was empty.\nPlease enter someting...')
            return jsonify(result=result)
        r1, elapsed_time = chk_repeat(data1, data2, data_type='list')
        if r1 == []:
            result.append('Two files have no repeated contents.\n')
            result.append('Duration for process: ' +
                          str(round(elapsed_time, 3)) + ' sec.')
        else:
            result.append(
                print_result(
                    r1,
                    title1='Two files have repeated content(s)',
                    elapsed_time=elapsed_time,
                    result2file='off',
                    display='off'))
    elif type == 'compare':
        if data2 == []:
            result.append('File2 was empty.\nPlease enter someting...')
            return jsonify(result=result)
        r1, elapsed_time1 = compare(data1, data2, data_type='list')
        r2, elapsed_time2 = compare(
            data2, data1, display_warning='off', data_type='list')
        elapsed_time = elapsed_time1 + elapsed_time2
        if r1 + r2 == []:
            result.append('File1 is same as File2.\n')
            result.append('Duration for process: ' +
                          str(round(elapsed_time, 3)) + ' sec.')
        elif r1 == []:
            result.append('File2完全包含File1。')
            result.append(
                print_result(
                    r2,
                    title1='File2比File1多以下内容',
                    elapsed_time=elapsed_time,
                    result2file='off',
                    display='off'))
        elif r2 == []:
            result.append('File1完全包含File2。')
            result.append(
                print_result(
                    r1,
                    title1='File1比File2多以下内容',
                    elapsed_time=elapsed_time,
                    result2file='off',
                    display='off'))
        else:
            result.append('两个文件互相有缺少内容')
            result.append(
                print_result(
                    r1,
                    title1='File1比File2多以下内容',
                    result2file='off',
                    display='off'))
            result.append(
                print_result(
                    r2,
                    title1='File2比File1多以下内容',
                    elapsed_time=elapsed_time,
                    result2file='off',
                    display='off'))
    elif type == 'chk_consecutive':
        try:
            r1, elapsed_time1 = chk_consecutive(data1, data_type='list')
            tmp, elapsed_time2 = chk_repeat(
                data1, display_warning='off', data_type='list')
            elapsed_time = elapsed_time1 + elapsed_time2
        except ValueError:
            result.append(
                '[Error]File1 contains non-numeric content. Please check and try again!'
            )
        else:
            if tmp != []:
                result.append(
                    '[Warning]File1 has repeated content(s).\nYou can "Check Repeat(Single File)" to check it.\n'
                )
            if r1 == []:
                result.append('File1 contains consecutive number.\n')
                result.append('Duration for process: ' +
                              str(round(elapsed_time, 3)) + ' sec.')
            else:
                result.append(
                    print_result(
                        r1,
                        title1='File1不连续',
                        title2='缺少以下元素：',
                        elapsed_time=elapsed_time,
                        result2file='off',
                        display='off'))
    return jsonify(result=result)


if __name__ == '__main__':
    app.run()
