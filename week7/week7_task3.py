# 旅游规划
def Find_min():
    min_index = -1
    min_miles = 99999
    min_cost = 99999
    for i in range(N):
        if visited[i] == 0:
            if miles[i] < min_miles:
                min_index = i
                min_miles = miles[i]
                min_cost = cost[i]
            elif (miles[i] == min_miles) and (cost[i] < min_cost):
                min_index = i
                min_cost = cost[i]
            else:
                continue
    return min_index


N, M, S, D = [int(x) for x in input().split()]
#  N:#cities   M:#railways  S:id of origins  D:id of destinations
# 可以看成是单源最短路问题
# 利用邻接表
network = []
visited = []
cost = []
miles = []
for i in range(N):
    network.append([])
    miles.append(99999)
    cost.append(99999)
    visited.append(0)
visited[S] = 1
cost[S] = 0
miles[S] = 0

for i in range(M):
    ori, des, lth, fee = [int(x) for x in input().split()]
    network[ori].append([des, lth, fee])
    network[des].append([ori, lth, fee])
now=S
while now!=D:

    visited[now] = 1  # 表示已经访问过
    for route in network[now]:
        des, lth, fee = route
        if visited[des]==0:
            if miles[des] > miles[now] + lth:
                miles[des] = miles[now] + lth
                cost[des] = cost[now] + fee
            elif miles[des] == (miles[now]+lth) and cost[des]>(cost[now]+fee):
                cost[des] = cost[now]+fee
            else:
                continue
    now = Find_min()

print(miles[D],cost[D])
