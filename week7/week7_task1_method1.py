def find_way(n):#利用dijkstra算法寻找每一个点到N的最短路，并记录最大值
    #dis保存原点到所有点的最短距离值
    dis = []#代表距离、是否visited
    for x in range(N + 1):
        dis.append([1000,0])
    dis[0]=[0,1]
    dis[n]=[0,1]
    #优先队列Q的每个结点保存verticle和s到该verticle的最短距离
    stack = []
    stack.append(n)
    #从Q的栈顶取出节点v和s到v的最短距离值
    #对所有从v出发的边的终点Y，更新dis[y]的距离
    while stack:
        min = 0
        for i in range(len(stack)):
            if dis[stack[i]][0] < dis[stack[min]][0]:
                min=i
        node = stack.pop(min)
        v=node
        dsv = dis[v][0]
        dis[v][1]=1
        for i in range(len(Network[v])):
            y = Network[v][i]
            vout,dvy=y[0],y[1]
            if dis[vout][1]==0:#if not visited
                if dis[vout][0]>dsv+dvy:
                    dis[vout][0] = dsv + dvy
                if vout not in stack:
                    stack.append(vout)
    longest_way = 0

    for i in range(N+1):
        if dis[i][1]==0:
            return 1000
        else:
            if dis[i][0]>longest_way:
                longest_way=dis[i][0]
    return longest_way

N, M = [int(x) for x in input().split()]#N,M代表动物数和咒语数

Network=[]
for i in range(N+1):#创建邻接表,长这个样子[[][[2,20]][[1,20]]],索引为0的位置空出来
    Network.append([])
for i in range(M):
    x,y,lenth = [int(x) for x in input().split()]
    Network[x].append([y,lenth])
    Network[y].append([x,lenth])

longest = []
for i in range(N):
    longest.append(find_way(i+1))
ans = min(longest)
if ans>=1000:
    print(0)
else:
    print(longest.index(ans)+1,ans)

'''
0	sample换数字，只有唯一解	答案正确	20 ms	3184KB
1	无解	答案正确	24 ms	3184KB
2	最大N的等边长环，解不唯一，输出最小编号	答案正确	39 ms	3184KB
3	最大N，最大M，随机完全图	运行超时	0 ms	0KB
'''
