#08-图9 关键活动
def toposort(Graph):
    vnum=N
    indegree, toposeq = [0]*vnum, []
    zerov=-1
    for vi in range(vnum):
        for v,w in graph[vi]:
            indegree[v]+=1
    for vi in range(vnum):
        if indegree[vi] == 0:
            indegree[vi]=zerov
            zerov=vi
    for n in range(vnum):
        if zerov==-1:
            return False
        vi = zerov
        zerov = indegree[zerov]
        toposeq.append(vi)
        if graph[vi]:
            for v, w in graph[vi]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    indegree[v] = zerov
                    zerov = v
        else:
            exit.append(vi)
    return toposeq
#N个节点，M条边
N, M = [int(x) for x in input().split()]#  # of activities check points
                                           # of activities
exit=[]
ee=[0]*N#earlest happening time
graph = []
for i in range(N):
    graph.append([])
for i in range(M):
    x,y,w=[int(x) for x in input().split()]
    x, y =x-1,y-1
    graph[x].append([y,w])
toposet = toposort(graph)
if not toposet:
    print(0)
else:
    for node in toposet:
        for edge in graph[node]:
            j, w = edge
            if ee[node] + w > ee[j]:
                ee[j] = ee[node] + w
    ans=max(ee)
    print(ans)
    eelast = ee.index(ans)

    le = [ee[eelast]] * N  # lastest happening time
    for item in exit:
        le[item]=ee[item]
    for k in range(N - 1, -1, -1):  # 逆拓扑排序
        i = toposet[k]
        for edge in graph[i]:
            j, w = edge
            if le[j] - w < le[i]:
                le[i] = le[j] - w

    for node in range(N):
        i=node
        for edge in graph[node][::-1]:  # 与输入顺序相反
            j =edge[0]
            if ee[i]==le[i] and ee[j]==le[j]:
                print(str(i+1) + '->' + str(j+1))

'''
0	sample 4条简单路径选1	答案正确	19 ms	3184KB
1	单起点和单终点，2条关键路径	答案正确	19 ms	3204KB
2	多起点和多终点	答案错误	18 ms	3184KB
3	不可行	答案正确	22 ms	3184KB
4	最大N，简单回路不可行	答案正确	22 ms	3424KB
5	最大N，随机，可行	答案错误	19 ms	3184KB
'''
