#!/usr/bin/python3

def file2list(file):
    l=[]
    data=file.readlines()
    for line in data:
        temp=line.split()
        l.append(temp[0])
    l.sort()
    return l

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

file1=open('file1.txt','r')
file2=open('file2.txt','r')
a=file2list(file1)
b=file2list(file2)
c=compare(a,b)
file1.close()
file2.close()
print('结果相差',len(c),'条记录')
result=open('output.txt','w')
for line in c:
    result.write(line+'\n')
result.close()


