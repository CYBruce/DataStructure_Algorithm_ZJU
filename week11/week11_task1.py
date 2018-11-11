#11-散列1 电话聊天狂人
def ScanAndOutput(hashtable):
    MinPhone,MaxCnt,PCnt=(0,0,0)
    for i in range(len(hashtable)):
        Ptr = hashtable[i]
        if len(Ptr)!=0:
            for users in Ptr:
                if users[1]>MaxCnt:
                    MaxCnt=users[1]
                    MinPhone=users[0]
                    PCnt=1
                elif users[1]==MaxCnt:
                    MinPhone = min(users[0],MinPhone)
                    PCnt += 1
    if PCnt > 1:
        print(MinPhone,MaxCnt,end=' ')
        print(PCnt)
    else:
        print(MinPhone, MaxCnt)

def CreateTable(tablesize):
    H = [[] for i in range(N*2)]
    return H

def Insert(hash,num):
    position = num%100000%(N*2)
    for cell in hash[position]:
        if num == cell[0]:
            cell[1]+=1
            return True
    hash[position].append([num,1])


#主程序框架
N = int(input())
H = CreateTable(N*2)
for i in range(N):
    number1, number2 = [int(x) for x in input().split()]
    Insert(H,number1)
    Insert(H,number2)
ScanAndOutput(H)


'''
#11-散列1 电话聊天狂人
def ScanAndOutput(hashtable):
    MinPhone,MaxCnt,PCnt=(0,0,0)
    for keys in hashtable:
        if hashtable[keys]>MaxCnt:
            MaxCnt=hashtable[keys]
            MinPhone=keys
            PCnt=1
        elif hashtable[keys]==MaxCnt:
            MinPhone = min(keys,MinPhone)
            PCnt += 1
    if PCnt > 1:
        print(MinPhone,MaxCnt,end=' ')
        print(PCnt)
    else:
        print(MinPhone, MaxCnt)

def Insert(hash,num):
    for keys in H:
        if keys == num:
            hash[keys]+=1
            return True
    hash[num]=1


#主程序框架
N = int(input())
H = {}
for i in range(N):
    number1, number2 = [int(x) for x in input().split()]
    Insert(H,number1)
    Insert(H,number2)
ScanAndOutput(H)
'''
