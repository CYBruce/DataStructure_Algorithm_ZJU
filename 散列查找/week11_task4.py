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
mytable = [-1]*TSize
hash_table = [int(x) for x in input().split()]
