#11-散列4 Hashing - Hard Version （30 分）
'''
TSize = int(input())
mytable = [-1]*TSize
hash_table = [int(x) for x in input().split()]#存储的是字符
numbers = []
for number in hash_table:
    if number != -1:
        numbers.append(number)
numbers.sort()
ans = []
while(numbers):
    for i in range(len(numbers)):
        err = 0
        while mytable[(numbers[i]+err)%TSize]!=-1:
            err+=1
        position = (numbers[i]+err)%TSize
        if hash_table[position] == numbers[i]:
            mytable[position]=numbers[i]
            ans.append(numbers[i])
            numbers.pop(i)
            break
for i in range(len(ans)-1):
    print(ans[i],end=' ')
print(ans[-1])
#采用建立哈希表的方法，但是会超时
'''
#利用拓扑排序来解决问题
TSize = int(input())
hash_table = [int(x) for x in input().split()]
ConnectMap = {}
InDgree = {}
for ele in hash_table:
    if ele > -1:
        InDgree[ele] = 0
        ConnectMap[ele] = []
    #初始化入度表和邻接表
for num in InDgree:
    err = 0
    while hash_table[(num+err)%TSize] !=num:
        ConnectMap[hash_table[(num + err) % TSize]].append(num)
        err+=1
        InDgree[num]+=1
    #构建入度表和邻接表
queue = []
for number in InDgree:
    if InDgree[number]==0:
        queue.append(number)
ans = []
while queue:
    v = min(queue)
    queue.remove(v)
    ans.append(v)
    for w in ConnectMap[v]:
        InDgree[w]=InDgree[w]-1
        if InDgree[w]==0:
            queue.append(w)

for i in range(len(ans)-1):
    print(ans[i],end=' ')
print(ans[-1])
#最大N，但是只有少数值，有非-1的空位
