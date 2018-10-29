import math
N=int(input())
initial = [int(x) for x in input().split()]
middle = [int(x) for x in input().split()]
initial2=[x for x in initial]

def isincreasing(start,end):
    for i in range(start,end):
        if middle[i]>middle[i+1]:
            return False
    return True

def Insert(position):
    for j in range(position):
        if initial[position]<initial[j]:
            temp=initial.pop(position)
            initial.insert(j,temp)

def Insert_or_Merge():
    for i in range(1,N):
        Insert(i)
        if initial==middle:
            print('Insertion Sort')
            i+=1
            if i<=N-1:
                Insert(i)
            for i in range(N - 1):
                print(initial[i], end=' ')
            print(initial[N - 1])
            return 1
    print('Merge Sort')
    return 0


def Merge(L,R,RightEnd):
    new = []
    LeftEnd = R-1
    tem=L#存放结果的数组的初始位置
    NumElements = RightEnd-L+1
    while(L<=LeftEnd and R<=RightEnd):
        if initial2[L]<=initial2[R]:
            new.append(initial2[L])
            L+=1
        else:
            new.append(initial2[R])
            R+=1
    while(L<=LeftEnd):
        new.append(initial2[L])
        L += 1
    while(R<=RightEnd):
        new.append(initial2[R])
        R += 1
    for i in range(len(new)):
        initial2[RightEnd]=new[-i-1]
        RightEnd-=1

tag = Insert_or_Merge()
if tag==0:#Merge Sort
    length = 1
    while(length<N):
        for i in range(0,N,length*2):
            if i+length < N:
                Merge(i, i + length, min(N-1, i + 2 * length - 1))
        length*=2
        if initial2==middle:
            break
    for i in range(0, N, length*2):
        if i+length<N:
            Merge(i,i+length,min(N-1,i+2*length-1))
    for i in range(N - 1):
        print(initial2[i], end=' ')
    print(initial2[N - 1])

'''
0	sample 1 Ins 中间步骤，有不需要交换的元素	答案正确	20 ms	3184KB
1	sample 2 Mg 有不成双，有不需要交换的元素	答案正确	18 ms	3204KB
2	最小N, Ins 第一步没变	答案正确	18 ms	3184KB
3	最小N，Mg第一步	答案正确	33 ms	3252KB
4	最大N，Ins	答案正确	29 ms	3184KB
5	最大N，Mg，后面N位没变化	答案正确	22 ms	3312KB
6	卡住Mg检查片段长度的错误算法，连续长度有3种	答案正确	35 ms	3312KB
'''
