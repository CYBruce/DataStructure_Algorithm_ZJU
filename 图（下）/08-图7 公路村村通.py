#08-图7 公路村村通
def Find(x):
    while(reps[x]>0):
        x=reps[x]
    return x
def Union(r1,r2):
    if reps[r1]<=reps[r2]:
        reps[r1]+=reps[r2]
        reps[r2]=r1
    else:
        reps[r2] += reps[r1]
        reps[r1] = r2

def Kruskal(map):
    MST=[]#初始化最小生成树
    while(len(MST)<N-1 and len(paths)>1):
        x,y,cost = map.pop(0)
        root1 = Find(x)
        root2 = Find(y)
        if root1!=root2:
            Union(root1,root2)
            MST.append(cost)
    if(len(MST)==N-1):
        print(sum(MST))
    else:
        print(-1)

N, M = [int(x) for x in input().split()]
paths = [[0,0,99999]]
reps=[]
for i in range(N+1):
    reps.append(-1)#建立相应的并查集
for i in range(M):
    paths.append([int(x) for x in input().split()])#x,y,cost
paths.sort(key=lambda x:x[2])
Kruskal(paths)
'''
0	sample换数字，各种回路判断	答案正确	29 ms	3056KB
1	M<N-1，不可能有生成树	答案正确	17 ms	3120KB
2	M达到N-1，但是图不连通	答案正确	18 ms	3096KB
3	最大N和M，连通	答案正确	34 ms	3744KB
4	最大N和M，不连通	答案正确	33 ms	3808KB
'''
