import math
#给出一个序列，找到满搜索树的根节点
def find_root(N):
    #如果是满二叉树，第n层应该有（2^n-1）个节点，1000个节点最多有10层
    level_num = math.ceil(math.log2(len(N)+1))
    unused = 2**level_num-1-len(N)
    if unused==0:#如果全部用完的话那根节点就是中心节点
        ans.append(N[math.floor(len(N)/2)])
        return math.floor(len(N)/2)
    elif unused>2**(level_num-2):#说明右边全空
        ans.append(N[len(N)-2**(level_num-2)])
        return len(N)-2**(level_num-2)
    else:#说明左边全满
        ans.append(N[2**(level_num -1)-1])
        return 2**(level_num -1)-1
ans=[]#存放答案
lth = int(input())
sequence = [int(x) for x in input().split()]
sequence.sort()#sort first
queue=[]
queue.append(sequence)
while(len(ans)<lth):
    now = queue.pop(0)
    root = find_root(now)
    if root!=0:
        queue.append(now[:root])
    if root!=len(now):
        queue.append(now[(root+1):])

for i in range(len(ans)-1):
    print(ans[i],end = ' ')
print(ans[len(ans)-1])






