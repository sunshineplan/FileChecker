#!/usr/bin/python3
# coding:utf-8

def precheck(list_data):
    data=[i.strip() for i in list_data]     #删除空格
    data=[i for i in data if i!='']         #删除空值
    output=sort_data(data)
    return output
    
def sort_data(list_data):
    #output=sorted(list_data, key=lambda item:(int(item.partition(' ')[0]) if item[0].isdigit() else float('inf'), item))
    output=sorted(list_data)
    return output

def print_result(result,title1='',title2='result:',ext='',elapsed_time=-1,result2file='on',display='on'):
    content=[]
    record=len(result)
    content.append(title1)
    content.append('\nTotal '+str(record)+' record(s)\n')
    content.append(title2)
    filename='result'+ext+'.txt'
    if record>17 and result2file=='on':
        list2file(content+result,filename)
        content.append('由于结果太大，已将其输出到'+filename)
    else:
        content=content+result
    if elapsed_time>=0:
        content.append('\n本次处理耗时'+str(round(elapsed_time,3))+'秒')
    if display=='on':
        print('\n'.join(content))
        return 0
    return content
