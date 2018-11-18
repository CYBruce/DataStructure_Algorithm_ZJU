def getinput(num):
    tree = []
    for i in range(num):
        type_in = input().split()
        name,left,right = type_in[0],type_in[1],type_in[2]
        tree.append([name,left,right])
    return tree

node_num1 = int(input())
tree1 = getinput(node_num1)
names1 = []
lefts1 = []
rights1 = []
for i in range(node_num1):
    names1.append(tree1[i][0])
    lefts1.append(tree1[i][1])
    rights1.append(tree1[i][2])
node_num2 = int(input())
tree2 = getinput(node_num2)
names2 = []
lefts2 = []
rights2 = []
for i in range(node_num2):
    names2.append(tree2[i][0])
    lefts2.append(tree2[i][1])
    rights2.append(tree2[i][2])

def find_root(tree):
    nodes = len(tree)
    sons = []
    for i in range(nodes):
        sons.append(tree[i][1])
        sons.append(tree[i][2])
    for i in range(nodes):
        if str(i) not in sons:
            return i


def if_same(t1,t2):
    root1 = find_root(t1)
    root2 = find_root(t2)
    if(len(t1)==0 and len(t2)==0):
        return 'Yes'
    #节点个数相同并且根节点相同才有可能同构
    elif(len(t1)==len(t2) and t1[root1][0]==t2[root2][0]):
        for i in range(node_num1):
            if(i != root1):#考虑每一个非根节点的节点的父节点是否一致
                this_node = t1[i][0]#这个节点的名字
                if str(i) in lefts1:
                    t1_father_where = lefts1.index(str(i))
                else:
                    t1_father_where = rights1.index(str(i))
                t1_father = t1[t1_father_where][0]
                i2 = names2.index(this_node)
                if str(i2) in lefts2:
                    t2_father_where = lefts2.index(str(i2))
                else:
                    t2_father_where = rights2.index(str(i2))
                t2_father = t2[t2_father_where][0]
                if(t2_father != t1_father):
                    return 'No'
        return 'Yes'

    else:
        return 'No'


print(if_same(tree1,tree2))
