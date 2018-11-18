MSize,N = [int(x) for x in input().split()]
def isPrime(n):
    if n == 1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

def FindMinPrime(msize):
    ans = msize
    while(not isPrime(ans)):
        ans+=1
    return ans
def Insert(x):
    position = x%TSize
    i=0
    while(i<=TSize):
        if hash_table[(position+i**2)%TSize]<0:
            hash_table[(position+i**2)%TSize]=x
            ans.append((position+i**2)%TSize)
            return True
        i+=1
    ans.append('-')


TSize = FindMinPrime(MSize)
hash_table = [-1]*TSize
nums = [int(x) for x in input().split()]
ans = []
for num in nums:
    Insert(num)
for i in range(N-1):
    print(ans[i],end=' ')
print(ans[-1])
