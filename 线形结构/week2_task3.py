#Reversing Linked List  https://pintia.cn/problem-sets/1010070491934568448/problems/1037889290772254722#p-4
def reverseK(START,TOTAL,K,ADDRESS,DATA,NEXT):
    times = int(TOTAL/K) #反转的次数
    ori_address = START #当前的位置
    answer = []
    if(TOTAL==1):
        print(ADDRESS[0],DATA[0],NEXT[0])
        return 0
    else:
        for i in range(times):
            print_list=[]
            for j in range(K):
                index = ADDRESS.index(ori_address)
                print_list.append([ADDRESS[index],DATA[index],NEXT[index]])
                ori_address = NEXT[index]
            #倒序输出当前存储的内容
            for m in range(K):
                answer.append(print_list[K-1-m])
        while(ori_address!='-1'):
            index = ADDRESS.index(ori_address)
            answer.append([ADDRESS[index],DATA[index],NEXT[index]])
            ori_address = NEXT[index]
        for j in range(len(answer)-1):
            print(answer[j][0],answer[j][1],answer[j+1][0])
        print(answer[j+1][0],answer[j+1][1],-1)
        return 0


'''
ls = input().split()
start = ls[0]
total = int(ls[1])
reverse_num = int(ls[2])
address = []
data = []
Next = []

#输入数据
for i in range(total):
    ls = input().split()
    address.append(ls[0])
    data.append(int(ls[1]))
    Next.append(ls[2])
print(start,total,reverse_num,address,data,Next)

reverseK(start,total,reverse_num,address,data,Next)
'''
reverseK('00100',1,1,['00100'],[4],[ '-1', '00000', '68237', '33218'])
'''
0	sample 有尾巴不反转, 地址取上下界	答案正确	30 ms	3312KB
1	正好全反转	答案正确	25 ms	3204KB
2	K=N全反转	答案正确	29 ms	3116KB
3	K=1不用反转	答案正确	17 ms	3312KB
4	N=1 最小case	答案正确	17 ms	3184KB
5	最大N,最后剩K-1不反转	运行超时	0 ms	0KB
6	有多余结点不在链表上	非零返回	30 ms	3120KB'''
