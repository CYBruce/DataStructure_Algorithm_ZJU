#File Transfer
network = []
num = int(input())
for i in range(num):
    network.append(-1)
network.append(-1)

def Find(x):
    while(network[x]>0):
        x=network[x]
    return x

def check(i,j):
    if Find(i)==Find(j):
        return True
    else:
        return False

def check_connected():
    counter=-1
    for unit in network:
        if unit<0:
            counter+=1
    if counter==1:
        print('The network is connected.')
    else:
        print('There are',counter,'components.')

def Union(r1,r2):
    if network[r1]<=network[r2]:
        network[r1]+=network[r2]
        network[r2]=r1
    else:
        network[r2] += network[r1]
        network[r1] = r2


def get_input(i,j):
    root1=Find(i)
    root2 = Find(j)
    if root1!=root2:
        Union(root1,root2)

command = input().split()
while(command[0]!='S'):
    if(command[0]=='I'):
        get_input(int(command[1]),int(command[2]))
    if(command[0]=='C'):
        if check(int(command[1]),int(command[2])):
            print('yes')
        else:
            print('no')
    command=input().split()

check_connected()

'''
#v1
import numpy as np
def check(i,j):
    return True

def check_connected():
    if True:
        print('The network is connected.')
    else:
        print('There are ' + 2 + ' components.')

num = int(input())
network = np.zeros(num)
command = input().split()
while(command[0]!='S'):
    if(command[0]=='I'):
        network[int(command[1])-1,int(command[2])-1]=1
        network[int(command[2])-1,int(command[1])-1]=1
    if(command[0]=='C'):
        if check(int(command[1])-1,int(command[2])-1):
            print('yes')
        else:
            print('no')
    command=input().split()

check_connected()

#v2
def check(i,j):
    for sub in network:
        if i in sub and j in sub:
            return True
    return False

def check_connected():
    if len(network)==1 and len(network[0]==num):
        print('The network is connected.')
    else:
        units=0
        for sub in network:
            units+=len(sub)
        print('There are',(len(network)+num-units),'components.')

def get_input(i,j):
    for sub in network:
        if i in sub or j in sub:
            if i in sub: sub.append(j)
            else: sub.append(i)
            return True
    network.append([i,j])


command = input().split()
while(command[0]!='S'):
    if(command[0]=='I'):
        get_input(int(command[1]),int(command[2]))
    if(command[0]=='C'):
        if check(int(command[1]),int(command[2])):
            print('yes')
        else:
            print('no')
    command=input().split()

check_connected()
'''
'''
0	sample 1 合并2个集合，最后不连通	答案错误	30 ms	3204KB
1	sample 2 最后连通	答案错误	33 ms	3128KB
2	最小N，无连通操作	答案正确	19 ms	3056KB
3	最大N，无操作	答案正确	18 ms	3128KB
4	最大N，递增链，卡不按大小union的	运行超时	0 ms	0KB
5	最大N，递减链，卡不按大小union的	运行超时	0 ms	0KB
6	最大N，两两合并，反复查最深结点，卡不压缩路径的	运行超时	0 ms	0KB
'''
