#Create Graph
N, M = [int(x) for x in input().split()]#N,M代表动物数和咒语数
Network=[]
for i in range(N):
    temp = []
    for j in range(N):
        if j==i:
            temp.append(0)
        else:
            temp.append(1000)
    Network.append(temp)
for i in range(M):
    x,y,lenth = [int(x) for x in input().split()]
    Network[x-1][y-1]=lenth
    Network[y-1][x-1] = lenth

#Floyd Algorithm
for k in range(N):
    for i in range(N):
        for j in range(N):
            if Network[i][k]+Network[k][j]<Network[i][j]:
                Network[i][j] = Network[i][k] + Network[k][j]

#Find Animal
def find_animal():
    MinDist = 1000
    for i in range(N):
        MaxDist = max(Network[i])
        if MaxDist == 1000:
            print('0')
            return 0
        elif MinDist > MaxDist:
            MinDist = MaxDist
            animal = i + 1
    print(animal, MinDist)

find_animal()
