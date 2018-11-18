#一开始思路搞错了，其实push进去的是先序顺序，pop出来的是中序；
#再通过先序和中序求后序

node_num = int(input())
PreOrder = []
stack = []
InOrder = []

def construct_series():
    j = 0
    #construct PreOrder and InOrder series
    while(j<node_num):
        str = input().split()
        if(str[0] == 'Push'):
            PreOrder.append(int(str[1]))
            stack.append(int(str[1]))
        else:
            InOrder.append(stack.pop(-1))
            j += 1



construct_series()
ans = []

def postorder_tranvers(List):#利用前序和中序求后序，利用递归
    if(len(List) != 0):
        root = 0
        position = 30
        for item in List:
            if (PreOrder.index(item) < position):
                position = PreOrder.index(item)
                root = item

        root_position = List.index(root)
        ans.append(root)
        if (root_position >= 0):
            postorder_tranvers(List[root_position + 1:])
        if (root_position <= len(List) - 1):
            postorder_tranvers(List[:root_position])


postorder_tranvers(InOrder)

for i in range(len(ans)-1):
    print(ans[len(ans)-1-i],end = ' ')
print(ans[0])
