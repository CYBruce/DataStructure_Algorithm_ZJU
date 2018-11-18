class tr(object):

    def __init__(self,data=None):
        self.right = None
        self.left = None
        self.data = data
        self.flag = 0


def inp():
    k = [int(x) for x in input().split()]
    if k[0] == 0:
        return False
    if k[0] != 0:
        len = int(k[0])
        num = int(k[1])
    lis = []
    for i in range(num+1):
        lis.append([int(x) for x in input().split()])
        return  lis

def get_inp():
    trs = []
    a = inp()
    while a:
        trs.append(a)
        a = inp()
        return trs

def check(root,tar):
    if not root:
        return False
    if tar == root.data:
        root.flag = 1
        return True
    if tar > root.data:
        if not root.data:
            return False
        return check(root.right,tar)
    if tar < root.data:
        if not root.flag:
            return False
        root.flag = 1
        return check(root.left,tar)

k = get_inp()
for tree_list in k:
    for tree_child_list in tree_list[1:]:
        st = build(tree_list[0])
        si = 1
        for x in tree_child_list:
            if not check(st,x):
                si = 0
                break
        if si:
            print('Yes')
        else:
            print('No')
