N = int(input())
nums = [int(x) for x in input().split()]
nums.sort()
for i in range(N-1):
  print(nums[i],end=' ')
print(nums[-1])
