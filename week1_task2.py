#Maximum Subsequence Sum
num = int(input())
ls = [int(x) for x in input().split()] #列表推导式
ThisSum = MaxSum = 0
head = ls[0]
tail = ls[num-1]
for i in range(num):
    ThisSum += ls[i]
    if((ThisSum > MaxSum)&(MaxSum == 0)):
        head = ls[i]
    if(ThisSum > MaxSum):
        MaxSum = ThisSum
        tail = ls[i]
    elif(ThisSum < 0):
        ThisSum = 0
if((MaxSum == 0)&(0 in ls)):
    head = tail =0
print(str(MaxSum)+' '+str(head)+' '+str(tail))
