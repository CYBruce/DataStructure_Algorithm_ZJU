#判断是否是同一棵二叉搜索树
#same=0代表目前两个搜索树还相同
same=0

def IsBST(X, Y):
    global same
    if len(X)==0 and len(Y)==0:
        return True
    else:
        if same == 1 or X[0] != Y[0] or len(X) != len(Y):
            same = 1
            return False
        elif (X == Y):  # 如果完全一样
            return True
        else:
            st_x = []  # smaller than X[0]
            bt_x = []
            st_y = []
            bt_y = []
            for i in range(len(X) - 1):
                if (X[i + 1] > X[0]):
                    bt_x.append(X[i + 1])
                else:
                    st_x.append(X[i + 1])
            for i in range(len(Y) - 1):
                if (Y[i + 1] > Y[0]):
                    bt_y.append(Y[i + 1])
                else:
                    st_y.append(Y[i + 1])
            IsBST(st_x, st_y)
            IsBST(bt_x, bt_y)


def get_input(N,L):
    global same
    LIST=[]
    real = input().split()
    for i in range(N):
        real[i] = int(real[i])#全部转换为Int
    for i in range(L):
        test = input().split()
        for j in range(N):
            test[j] = int(test[j])  # 全部转换为Int
        same = 0
        IsBST(real,test)
        if (same == 0):
            LIST.append('Yes')
        else:
            LIST.append('No')
    for i in range(len(LIST)):
        print(LIST[i])


first_in = input()
while(first_in != '0'):
    L_N  = first_in.split()
    get_input(int(L_N[0]), int(L_N[1]))
    first_in = input()

'''
0	sample 换顺序。有Yes，有No：根不同，子树根不同。树有单边、有双子树	答案正确 	22 ms	3160KB
1	最大N，多组合	 非零返回 19 ms	3184KB
2	N=1，只有1个节点	答案正确	20 ms	3312KB
3	卡只判断数字相对先后位置的错误算法	答案正确	18 ms	3184KB
'''
