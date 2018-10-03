#Huffman Codes
#定义节点类
class Node(object):
    def __init__(self,name=None,value=None):
        self._name=name
        self._value=value
        self._left=None
        self._right=None
        self._height=0
#定义哈夫曼树类
class HuffmanTree(object):
    def __init__(self,char_weights):
        self.a = [Node(part[0], part[1]) for part in char_weights]  # 根据输入的字符及其频数生成叶子节点
        while len(self.a) != 1:
            self.a.sort(key=lambda node: node._value, reverse=True)
            c = Node(value=(self.a[-1]._value + self.a[-2]._value))
            c._left = self.a.pop(-1)
            c._right = self.a.pop(-1)
            self.a.append(c)
        self.root = self.a[0]

    def cost(self):
        line=[self.root]
        cost=0
        while(len(line)!=0):
            out = line.pop(0)
            if (out._left==None) and (out._right==None):
                cost+=out._height*out._value
            if out._left!=None:
                out._left._height=out._height+1
                line.append(out._left)
            if out._right!=None:
                out._right._height = out._height + 1
                line.append(out._right)
        return cost

def isfore(x,y):
    len_x=len(x)
    len_y=len(y)
    if len_x<len_y:
        if x==y[:len_x]:
            return True
    else:
        if y==x[:len_y]:
            return True
    return False

def check():
    use=[]
    for i in range(code_num):
        character , code=input().split()
        use.append([character,code])
    #判断是否满足最小cost
    #判断是否有前缀码
    cost=0
    for i in range(code_num):
        find = characters.index(use[i][0])
        fre = frenquencys[find]#出现频率
        lth = len(use[i][1])#编码长度
        cost+=(fre*lth)
    if cost!=mincost:
        return False

    for i in range(code_num - 1):
        test1 = use[i][1]
        for j in range(i + 1, code_num):
            test2 = use[j][1]
            if isfore(test1, test2):
                return False
    return True


code_num = int(input())
get_input = input().split()
characters=[]
frenquencys=[]
char_weights=[]
for i in range(code_num):
    characters.append(get_input[2*i])
    frenquencys.append(int(get_input[2*i+1]))
    char_weights.append((get_input[2*i],int(get_input[2*i+1])))
#计算出最小的cost,利用最小堆
mincost=HuffmanTree(char_weights).cost()

stu_num=int(input())
for i in range(stu_num):
    if check():
        print('Yes')
    else:
        print('No')

'''
0	sample 有并列、多分支，有长度错、长度对但是前缀错；仅英文大写字符	答案正确	34 ms	3332KB
1	小写字母，01反、且2点对换；有2点重合	答案正确	19 ms	3332KB
2	几组编码不等长，都对；等长但前缀错误；code长度超过N	答案正确	18 ms	3344KB
3	最大N&M，code长度等于63	运行超时	0 ms	0KB
4	最小N&M	答案正确	17 ms	3440KB
5	编码的字符是双数个，而提交采用的是等长编码。卡仅判断叶结点和度的错误算法	答案正确	32 ms	3184KB
6	非Huffman编码，但是正确；没有停在叶子上	答案正确	19 ms	3332KB
'''
