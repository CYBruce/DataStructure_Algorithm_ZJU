#08-图8 How Long Does It Take
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
        for v,w in graph[vi]:
            indegree[v]-=1
            if indegree[v]==0:
                indegree[v]=zerov
                zerov = v
    return toposeq
#N个节点，M条边
N, M = [int(x) for x in input().split()]#  # of activities check points
                                           # of activities
ee=[0]*N#earlest happening time
graph = []
for i in range(N):
    graph.append([])
for i in range(M):
    x,y,w=[int(x) for x in input().split()]
    graph[x].append([y,w])
toposet = toposort(graph)
if not toposet:
    print('Impossible')
else:
    for node in toposet:
        for edge in graph[node]:
            j, w = edge
            if ee[node] + w > ee[j]:
                ee[j] = ee[node] + w
    print(max(ee))
'''
0	sample 1 一般情况，有0边，单个起点和单个终点	答案正确	34 ms	3112KB
1	sample 2 有环	答案正确	18 ms	3184KB
2	多个起点和多个终点	答案正确	19 ms	3148KB
3	最大N，不可行	答案正确	18 ms	3220KB
4	最大N，可行	答案正确	20 ms	3552KB
'''
