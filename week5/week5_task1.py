#建立最小堆,堆其实就是一种完全二叉树
heap=[]
def in_heap(X):
    heap.append(X)
    position = len(heap)-1
    while(position>0):
        if heap[position]<heap[(position-1)//2]:
            heap[position],heap[(position-1)//2]=heap[(position-1)//2],heap[position]
            position=(position-1)//2
        else:
            return True

N, M = [int(x) for x in input().split()]
elements = [int(x) for x in input().split()]
for element in elements:
    in_heap(element)

find = [int(x)-1 for x in input().split()]

for i in find:
    ans=[]
    while(i>=0):
        ans.append(heap[i])
        i=(i-1)//2

    for i in range(len(ans) - 1):
        print(ans[i], end=' ')
    print(ans[len(ans) - 1])
