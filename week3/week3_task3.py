node_num = int(input())
tree = []
stack = []

def construct_tree():
    i = 0
    j = 0
    tag = 0
    while(j<node_num):
        str = input().split()
        if(str[0] == 'Push'):
            tree.append([str[1]])
            if(i!=0):
                tree[tag].append(i)
            stack.append(i)
            tag = i
            i += 1
        else:
            tag = stack.pop(-1)
            j+=1

construct_tree()
ans = []

def postorder_tranvers(T):#后序遍历树,练习一下递归
    if(len(tree[T])==1):
        ans.append(tree[T][0])
    elif(len(tree[T])==2):
        postorder_tranvers(tree[T][1])
        ans.append(tree[T][0])
    else:
        postorder_tranvers(tree[T][1])
        postorder_tranvers(tree[T][2])
        ans.append(tree[T][0])


postorder_tranvers(0)
for i in range(len(ans)-1):
    print(ans[i][0],end = ' ')
print(ans[len(ans)-1][0])
