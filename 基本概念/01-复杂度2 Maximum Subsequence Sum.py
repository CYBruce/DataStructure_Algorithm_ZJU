#Maximum Subsequence Sum
num = int(input())
ls = [int(x) for x in input().split()] #列表推导式
ThisSum = MaxSum = 0
head = ls[0]
tail = ls[num-1]
tag=0
for i in range(num):
    if((ls[i] >= 0) and tag==0):
        this_head = ls[i]
        tag=1
    ThisSum += ls[i]
    if(ThisSum > MaxSum):
        MaxSum = ThisSum
        tail = ls[i]
        head = this_head
    elif(ThisSum < 0):
        ThisSum = 0
        tag=0
if(MaxSum == 0 and 0 in ls):
    head = tail =0
print(str(MaxSum)+' '+str(head)+' '+str(tail))
