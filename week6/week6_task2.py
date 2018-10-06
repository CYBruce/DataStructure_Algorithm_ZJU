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
    elif (cor[0])**2+(cor[1])**2<=(D+15)**2:
        return True
    else:
        return False

def if_land(cor):
    if (cor[0]<=-50+D) or (cor[0]>=50-D) or (cor[1]<=-50+D) or (cor[1]>=50-D):
        return True
    else:
        return False

def DFS(node):#node is coordinate, type: list
    ans = False
    visited.append(node)
    if if_land(node):
        ans=True
    else:
        for neighbor in nodes:
            if neighbor not in visited and within_dist(node,neighbor):
                ans = DFS(neighbor)
                if ans:
                    break
    return ans



N, D = [int(x) for x in input().split()]
nodes = []
for i in range(N):
    nodes.append([int(x) for x in input().split()])
visited=[]
flag=0
if D>=50:
    print('Yes')
else:
    for node in nodes:
        if (node not in visited) and within_first_jump(node):
            if DFS(node):
                flag = 1
                print('Yes')
                break
    if flag == 0:
        print('No')
