#一元多项式的乘法与加法运算
'''
多项式加法和乘法问题https://pintia.cn/problem-sets/1010070491934568448/problems/1037889290772254721#p-3
这段代码写了好久，一直都在抠细节，几点感想：
1. Python中逻辑关系直接用and or not,省的搞不清楚还麻烦
2.
      1 coef = [10,20,0,4,3,1]
      2 for i in range(len(coef)):
----> 3     if(coef[i] == 0):
      4         del coef[i]
      5     i+=1

IndexError: list index out of range
至今不知道错误的原因，所以对于list循环来说，尽量不要这样搞了，直接for item in list

3.养成结构化编程的好习惯，写函数容易打理
4.这道题并没有拿满分，还有一小点找不到错误所在

算法流程：
先写加法方程，注意要删掉为0的项
乘法相当于p1每一项与p2乘之后再相加
输出方程：判断是否为空，如果空按要求输出，
        如果不空从头到尾输出，注意最后一个数字后面不能有空格

'''


def polymerge(coef1, poly1, coef2, poly2):
    coef_ans = []
    poly_ans = []
    m = 0
    n = 0
    while ((m <= (len(poly1) - 1)) and (n <= (len(poly2) - 1))):
        if (poly1[m] > poly2[n]):
            coef_ans.append(coef1[m])
            poly_ans.append(poly1[m])
            m += 1
        elif (poly1[m] < poly2[n]):
            coef_ans.append(coef2[n])
            poly_ans.append(poly2[n])
            n += 1
        else:
            coef_ans.append(coef1[m] + coef2[n])
            poly_ans.append(poly1[m])
            m += 1
            n += 1
    if (m <= len(coef1) - 1):
        for item in coef1[m:]:
            coef_ans.append(item)
        for item in poly1[m:]:
            poly_ans.append(item)
    if (n <= len(coef2) - 1):
        for item in coef2[n:]:
            coef_ans.append(item)
        for item in poly2[n:]:
            poly_ans.append(item)
    return coef_ans, poly_ans


ls1 = [int(x) for x in input().split()]  # 列表推导式
ls2 = [int(x) for x in input().split()]
# 先将系数和次数放在两个数组中
len_1 = ls1[0]
uses_1 = ls1[1:]
coef_1 = uses_1[0::2]
poly_1 = uses_1[1::2]
len_2 = ls2[0]
uses_2 = ls2[1:]
coef_2 = uses_2[0::2]
poly_2 = uses_2[1::2]

# 乘法推导
i = j = 0
coef = []
poly = []
for i in range(len_1):
    poly_temp = []
    coef_temp = []
    for j in range(len_2):
        coef_temp.append(coef_1[i] * coef_2[j])
        poly_temp.append(poly_1[i] + poly_2[j])
    coef, poly = polymerge(coef, poly, coef_temp, poly_temp)

i = 0
# 这里存在一些问题，考虑逻辑的话有些零值会补位然后就可能没有被删除
# 考虑改成while(0 in coef)解决
while (0 in coef):
    i = 0
    for item in coef:
        if (item == 0):
            del coef[i]
            del poly[i]
        i += 1

tag = 0
if len(coef) == 0:
    print('0 0')
else:
    for i in range(len(coef)):
        if (coef[i] != 0):
            tag = 1
            if i == (len(coef) - 1):
                print(coef[i], end=' ')
                print(poly[i], end='')
            else:
                print(coef[i], end=' ')
                print(poly[i], end=' ')
if (tag == 0):
    print('0 0')

# 多项式加法计算过程
i = j = 0
coef = []
poly = []
while ((i <= len_1 - 1) & (j <= len_2 - 1)):
    if poly_1[i] > poly_2[j]:
        coef.append(coef_1[i])
        poly.append(poly_1[i])
        i += 1
    if poly_1[i] < poly_2[j]:
        coef.append(coef_2[j])
        poly.append(poly_2[j])
        j += 1
    if poly_1[i] == poly_2[j]:
        coef.append(coef_1[i] + coef_2[j])
        poly.append(poly_1[i])
        i += 1
        j += 1
if (i <= len_1 - 1):
    for item in coef_1[i:]:
        coef.append(item)
    for item in poly_1[i:]:
        poly.append(item)
if (j <= len_2 - 1):
    for item in coef_2[j:]:
        coef.append(item)
    for item in poly_2[j:]:
        poly.append(item)
print('')

while (0 in coef):
    i = 0
    for item in coef:
        if (item == 0):
            del coef[i]
            del poly[i]
        i += 1

tag = 0
if len(coef) == 0:
    print('0 0')
else:
    for i in range(len(coef)):
        if (coef[i] != 0):
            tag = 1
            if i == (len(coef) - 1):
                print(coef[i], end=' ')
                print(poly[i], end='')
            else:
                print(coef[i], end=' ')
                print(poly[i], end=' ')
if (tag == 0):
    print('0 0')

# 0	sample换个数字	答案正确	23 ms	3312KB
# 1	同类项合并时有抵消	答案正确	18 ms	3568KB
# 2	系数和指数取上限，结果有零多项式	答案正确	31 ms	3448KB
# 3	输入有零多项式和常数多项式	答案错误	27 ms	3440KB
