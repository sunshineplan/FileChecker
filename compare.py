#!/usr/bin/python3

def file2list(filename):
    file=open(filename)
    data=file.readlines()
    file.close()
    count=0
    for line in data:
        line=line.strip('\n')#删除\n
        line=line.strip()#删除空格
        data[count]=line
        count+=1
    output=[a for a in data if a!='']#删除空值
    output.sort()
    return output

def list2file(l,filename):
    file=open(filename,'w')
    for line in l:
        file.write(str(line)+'\n')
    file.close()
    return 0

def chk_repeat(filename):
    file=file2list(filename)
    repeat=[]
    for a in file:
        if file.count(a)!=1:
            repeat.append(str(a)+'重复了'+str(file.count(a))+'次')
    output=list(set(repeat))#删除重复值
    output.sort()
    if output!=[]:
        changed=list(set(file))#将去重后的文件输出，文件名在原来的基础上加"_changed"后缀
        changed.sort()
        changedfile=list2file(changed,filename[:filename.rindex('.')]+'_changed'+filename[filename.rindex('.'):])
    return output

def compare(file1,file2):
    print('file1要包含file2')
    c1=0
    c2=0
    result=[]
    while c2<len(file2):
        if file1[c1]==file2[c2]:
            c1+=1
            c2+=1
        else:
            result.append(file1[c1])
            c1+=1
    return result

a=file2list('file1.txt')
b=file2list('file2.txt')
c=compare(a,b)
print('结果相差',len(c),'条记录')
list2file(c,'output.txt')


