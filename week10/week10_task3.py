#N个数字的排列由若干个独立的环组成
N = int(input())
sequence = [int(x) for x in input().split()]
check = [0 for x in range(N)]
swaps = 0
ans=0
for i in range(N):
    if check[i]==1 or sequence[i]==i:#不需要交换的情况
        continue
    else:
        check[i] = 1
        flag=sequence[i]
        ele_num=1
        while(i!=flag):
            check[flag] = 1
            flag = sequence[flag]
            ele_num+=1
        ans+=(ele_num+1)
if sequence[0]==0:
    print(max(0,ans))
else:
    print(max(0,ans-2))

