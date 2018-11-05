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
print(users)
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
    print('{} {} {}'.format(flag, str(users[index][0]).zfill(5),score_memory),end=' ')
    for i in range(q_num-1):
        print(users[index][1][i],end=' ')
    print(users[index][1][-1])
    count+=1



