#列出连通集
N, E = [int(x) for x in input().split()]
#建立邻接表
neighbor_list = []
nodes=list(range(N))

for i in nodes:
    neighbor_list.append([])

for i in range(E):
    x1,x2 = [int(x) for x in input().split()]
    neighbor_list[x1].append(x2)
    neighbor_list[x2].append(x1)

#DFS
stack=[]
nodes_DFS = nodes[:]
while(len(nodes_DFS)!=0):
    stack.append(nodes_DFS[0])
    ans = []
    while(len(stack)!=0):
        node = stack[-1]
        if node not in ans:
            ans.append(node)
            nodes_DFS.remove(node)
        find_flag=0
        for i in nodes_DFS:
            if i in neighbor_list[node]:
                stack.append(i)
                find_flag=1
                break
        if find_flag==0:
            stack.pop(-1)
    print('{',end=' ')
    for i in range(len(ans) - 1):
        print(ans[i], end=' ')
    print(ans[len(ans) - 1],end=' }\n')


#BFS
queue=[]
nodes_BFS = nodes[:]
while(len(nodes_BFS)!=0):
    queue.append(nodes_BFS[0])
    ans = []
    while(len(queue)!=0):
        node = queue.pop(0)
        ans.append(node)
        nodes_BFS.remove(node)
        for i in nodes_BFS:
            if i in neighbor_list[node] and i not in queue:
                queue.append(i)
    print('{', end=' ')
    for i in range(len(ans) - 1):
        print(ans[i], end=' ')
    print(ans[len(ans) - 1], end=' }\n')

#continue是跳出本次循环，break才是跳出全部循环
