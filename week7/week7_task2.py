#Saving James Bond - Hard Version
#save 007

def within_dist(cor_1,cor_2):
    if D<=0:
        return False
    elif (cor_1[0]-cor_2[0])**2+(cor_1[1]-cor_2[1])**2<=D**2:
        return True
    else:
        return False

def within_first_jump(cor):
    if D<=0:
        return False
    elif (cor[0])**2+(cor[1])**2<=(D+7.5)**2:
        return True
    else:
        return False

def if_land(cor):
    if (cor[0]<=-50+D) or (cor[0]>=50-D) or (cor[1]<=-50+D) or (cor[1]>=50-D):
        return True
    else:
        return False

def Unweighted(net):
    for i in range(len(net)):
        if within_first_jump(net[i]):
            queue.append(i)
            dist[i]=1
    if D>=42.5:
        return -2
    #第一步能跳到的点
    while queue:
        V = queue.pop(0)
        if if_land(net[V]):
            return V
        for i in range(len(net)):
            if dist[i]==-1 and within_dist(net[V],net[i]):
                dist[i] = dist[V]+1
                path[i] = V
                queue.append(i)
    return -1

queue = []
N, D = [int(x) for x in input().split()]
nodes = []
path = []
dist=[]
for i in range(N):
    nodes.append([int(x) for x in input().split()])
    path.append(-1)
    dist.append(-1)
nodes.sort(key=lambda x:x[1]**2+x[0]**2) #nodes sort first
ans = Unweighted(nodes)

if ans==-1:
    print(0)
elif ans==-2:
    print(1)
else:
    print(dist[ans]+1)
    Route = []
    while ans!=-1:
        Route.append(nodes[ans])
        ans = path[ans]
    for node in Route[::-1]:
        print(node[0],node[1])

'''
0	sample1 多条最短路，同一点有多路，最近点无路，多连通	答案正确	33 ms	3184KB
1	sample 2 聚集型，均离岸远	答案正确	34 ms	3184KB
2	分散型，均跳不到，有在角上	答案正确	27 ms	3184KB
3	有一只在岸上，有一只在岛上，不能算在内	答案正确	20 ms	3184KB
4	最大N，sample1的复杂版，可选路径8条，后面要更新前面的最短路	答案正确	31 ms	3240KB
5	最小N，一步跳到岸	答案正确	18 ms	3184KB
'''
