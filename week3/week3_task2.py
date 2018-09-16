def getinput(num):
    tree = []
    for i in range(num):
        type_in = input().split()
        left,right = type_in[0],type_in[1]
        tree.append([left,right])
    return tree

node_num = int(input())
tree = getinput(node_num)

def find_root(t):
    sons = []
    for i in range(node_num):
        sons.append(tree[i][0])
        sons.append(tree[i][1])
    for i in range(node_num):
        if str(i) not in sons:
            return i

root = find_root(tree)
stack = []
ans = []
#利用层序遍历找叶节点
def InOrderTravel(T):
    stack.append(T)
    while(len(stack)!=0):
        T = stack.pop(0)
        if (tree[T][0] == '-' and tree[T][1] == '-'):
            ans.append(T)
        if (tree[T][0] != '-'):
            stack.append(int(tree[T][0]))
        if(tree[T][1] != '-'):
            stack.append(int(tree[T][1]))


InOrderTravel(root)
for i in range(len(ans)-1):
    print(ans[i],end = ' ')
print(ans[len(ans)-1])
