#六度空间


def BFS(node):
    visited = []
    for i in range(N+1):
        visited.append(0)
    queue=[]
    visited[node]=1
    queue.append(node)
    count=1
    level=0
    last=node
    while(len(queue)!=0):
        v = queue.pop(0)
        for w in neighbor_list[v]:
            if visited[w]==0:
                visited[w]=1
                queue.append(w)
                count+=1
                tail = w
        if v==last:
            level+=1
            last = tail
        if level==6:
            break
    return count


N, M = [int(x) for x in input().split()]
#分别表示社交网络图的结点数N、边数M
neighbor_list=[]
for i in range(N+1):
    #建立邻接表,从1开始，所以0为空
    neighbor_list.append([])
for i in range(M):
    x1, x2 = [int(x) for x in input().split()]
    neighbor_list[x1].append(x2)
    neighbor_list[x2].append(x1)

for i in range(1,N+1):
    count = BFS(i)
    print('{}: {:.2%}'.format(i,count/N))
