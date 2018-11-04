#利用桶排序
N = int(input())
age = [0 for x in range(51)]
ages = [int(x) for x in input().split()]
for i in ages:
  age[i]+=1
for i in range(51):
  if age[i]!=0:
    print(str(i)+':'+str(age[i]))
