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
'''
这道题要建立满二叉搜索树，考察了搜索树的同时也考察了层序遍历
层序遍历利用了队列，在一开始做题的时候陷入了迭代的怪圈搞了很久（迭代更适合前中后序遍历），
迭代在有些情况好很好用，但在本题中实现的话有点绕，所以就放弃了

因为二叉搜索树是按顺序排列的，所以先进行了排序
这道算法题实现的思想就是先找根节点，然后再找左右子树的根节点，
满二叉书结构比较简单，可以计算出根节点在什么位置
'''




