#!/usr/bin/python3

def file2list(filename):
    file=open(filename)
    data=file.readlines()
    file.close()
    c=0
    for line in data:
        line=line.strip('\n')
        data[c]=line
        c+=1
    data.sort()
    return data

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
result=open('output.txt','w')
for line in c:
    result.write(line+'\n')
result.close()


