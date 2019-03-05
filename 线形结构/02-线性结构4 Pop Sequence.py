#POP SEQUENCE
def check_sub(L2):
    for j in range(len(L2)-1):
        if(L2[j]<=L2[j+1]):
            return 0
    return 1

def check(seq,M,L):
    for m in range(L):
        count = 0#计数小于本位置数字的个数，不能超过M
        n = m+1
        temp = []
        while(n<L):
            if(seq[n]<seq[m]):
                count+=1
                temp.append(seq[n])
            n+=1
        if(count>=M):
            return 'NO'
        if(check_sub(temp)==0):
            return 'NO'
    return 'YES'


def main():
    max_cap, length, num_check = [int(x) for x in input().split()]
    seqs = []
    for i in range(num_check):
        seqs.append([int(x) for x in input().split()])
    for i in range(num_check):
        print(check(seqs[i], max_cap, length))
        
if __name__ == '__main__':
    main()
    
