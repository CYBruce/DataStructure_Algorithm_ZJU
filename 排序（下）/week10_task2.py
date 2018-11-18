user_num,q_num,submission_num = [int(x) for x in input().split()]
full_mark=[int(x) for x in input().split()]
marks = [-2 for x in range(len(full_mark))]#-2代表未提交
users = [[x,[i for i in marks],0,0] for x in range(user_num+1)]#id, marks, full_mark problems, score, unpassed

for i in range(submission_num):
    user_id,problem_id,partial_score_obtained=[int(x) for x in input().split()]
    if partial_score_obtained>users[user_id][1][problem_id-1]:
        delta = max(0,partial_score_obtained) - max(0,users[user_id][1][problem_id-1])
        users[user_id][1][problem_id - 1] = partial_score_obtained
        users[user_id][3]=users[user_id][3]+delta
        if partial_score_obtained == full_mark[problem_id-1]:
            users[user_id][2] += 1

#sort part
users.sort(key=lambda x:(x[3],x[2]),reverse=1)
#print part
flag=1
count=1
score_memory = users[0][3]
for index in range(user_num+1):
    counter=0
    for j in range(q_num):
        if users[index][1][j]==-2:
            users[index][1][j]='-'
            counter+=1
        elif users[index][1][j]==-1:
            users[index][1][j]=0
            counter+=1
    if counter==q_num:
        continue
    if users[index][3]!=score_memory:
        score_memory=users[index][3]
        flag=count
    print('{} {:0>5d} {}'.format(flag, users[index][0],score_memory),end=' ')
    for i in range(q_num-1):
        print(users[index][1][i],end=' ')
    print(users[index][1][-1])
    count+=1


'''
2018/11/6 08:35:53	
答案正确
25	10-排序5	C++ (g++)	34 ms	4_bruce
测试点	提示	结果	耗时	内存
0	sample 部分分；后面提交没有前面高；并列按id排；没提交；编译不过；有人有题目没提交过；提交0分、提交-1	答案正确	3 ms	384KB
1	最小N	答案正确	2 ms	384KB
2	K最小，有0分	答案正确	2 ms	384KB
3	M最小	答案正确	5 ms	1152KB
4	最大随机测试，有满分的题目重复提交	答案正确	34 ms	1024KB
'''
