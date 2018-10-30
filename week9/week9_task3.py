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

def Insert_or_Heap():
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
    print('Heap Sort')
    return 0

def PerceDown(position,length):
    while(2*position+1<length):#如果有子节点
        if (2*position+2<length and middle[2*position+2]>middle[2*position+1]):#如果右子节点存在并且更大
            middle[position],middle[2*position+2]=middle[2*position+2],middle[position]
            position=2*position+2
        elif(middle[2*position+1]>middle[position]):
            middle[position], middle[2 * position + 1] = middle[2 * position + 1],middle[position]
            position=2*position+1
        else:
            break


tag = Insert_or_Heap()
if tag==0:#Heap Sort
    for i in range(1,N):
        if middle[i]>middle[0]:
            middle[i-1], middle[0] = middle[0], middle[i-1]
            PerceDown(0, i-1)
            break
    for i in range(N - 1):
        print(middle[i], end=' ')
    print(middle[N-1])
