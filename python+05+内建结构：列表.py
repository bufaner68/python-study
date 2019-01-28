
# coding: utf-8

# # 内置数据结构（变量类型）
# - list
# - set
# - dict
# - tuple
# ## list（列表）
# - 一组由顺序的数据的组合
# - 创建列表
#     - 空列表

# In[8]:

# 1.创建空列表
l1 = []
# type是内部函数，负责打印出变量的类型
print(type(l1))
print(l1)
# 2.创建带值的列表
l2 = [100]
print(type(l2))
print(l2)
# 3.创建列表，带多个值
l3 = [100,6,8,90,89]
print(type(l3))
print(l3)
# 4.使用list()
l4 = list()
print(type(l4))
print(l4)


# ## 列表常用操作
# - 访问
#     - 使用下标操作（索引）
#     - 列表的位置从0开始
# - 分片操作

# In[10]:

# 下标访问列表
l = [1,4,2,3,5,6]
print(l[3])
print(l[0])


# In[15]:

# 分片操作
# 注意包含的范围，包含左边下标值，不包含右边
print(l[1:3])
# 下标值可以为空，表示左下标值为0，右下标为最大值加1，即截取到最后一位
print(l[:])
print(l[:4])
print(l[1:])


# In[19]:

# 分片可以控制增长幅度，默认增长幅度为1
print(l)
print(l[1:6:1])
print(l[1:6:2])
# 下标可以超出范围，超出的直接忽略，不再考虑
print(l[3:10:4])


# In[39]:

## 分片之负数下标
# 下标值增长幅度可以为负数
# 为负数，表明顺序为从右往左
# 最后一个数下标为-1，倒数第二个数为-2，以此类推
print(l[-7:-1])
# 默认分片是从左往右，如果左边范围大于右边，会打印出空
# 如果一定要左边大于右边，可以采用负步长
# 这个案例给list的正反颠倒提供了一种思路
print(l[-2:-6])
print(l[-2:-6:-1])
# 反向输出list
print(l[-1:-6:-1])


# ## 分片操作是产生一个新的list
#  - 内置函数id，负责显示一个数据或变量的唯一确定编号

# In[40]:

# id函数举例
a = 100
b = 200
print(id(a))
print(id(b))

c = a
print(id(c))

# 如果a跟c只想一份数据，则更改a的值同样也会更改c的值
# 但是，显示结果并非如此，为什么？
a = 101
print(a)
print(c)


# In[41]:

# 通过id可以直接判断出分片是从新生成了一份数据还是使用的同一份数据
l = [3,4,56,76,32,21,43,5]
ll = l[:]
lll = ll
# 如果两个id值一样，则表明分片产生的列表是使用的同一地址同一份数据
# 否则，则表明分片是从新生成了一份数据，即一个新的列表，然后把数值拷贝到新列表中
print(id(l))
print(id(ll))
print(id(lll))

# 通过id知道，ll和lll是同一份数据，验证代码如下
l[1] = 100
print(l)
print(ll)

ll[1] = 100
print(ll)
print(lll)


# # List ：列表操作
# - del：删除
# - +：链接两个列表
# - *：将n个列表链接
# - in，not in：判断成员是否在列表里

# In[2]:

# del 命令：删除列表或列表元素
a = [1,2,3,4,5,6]
del(a[2])
print(a)


# In[3]:

# del 删除
# 如果使用del之后，id的值和删除前不一样，则说明删除生成了一个新的list
a = [3,5,7,76]
print(id(a))
del(a[2])
print(id(a))
print(a)
# 删除列表元素是在愿列表内删除，并没有新生成一个列表


# In[4]:

# del一个变量后不能在继续使用此变量
del(a)
print(a)


# In[6]:

# 使用加号链接两个列表:+
a = [1,2,3]
b = [4,5]
v = ['a','b','v']
print(a+b+v)


# In[7]:

# 使用乘号操作列表:*
# 列表直接跟一个整数相乘 ，相当于把n个列表接在一起
a = [1,2,3,4]
c = a*3
print(c)


# In[8]:

# 成员资格运算:in, not in
# 就是判断一个元素是否在爱list里边
a = ['c','v','a','a']
print('v' in a)
print('b' not in a)


# ### 列表的遍历
# - for
# - while

# In[11]:

a = [1,2,3,4,5]
# name这个变量名是列表里的一个元素的代称，随便取，它与a[i]表示一样的含义
for name in a:
    # 挨个打印a里边的元素
    print(name)


# In[12]:

# java， c++ 程序员写的python代码是这样的
for i in range(0,len(a)):
    print(a[i])
    i += 1


# In[2]:

# range
# in 后面的变量要求是可以可迭代的内容
for i in range(1,10):
    print(i)

print(type(range(1,10)))


# In[1]:

# while循环访问list
# 一般不用while遍历list
a = [1,2,3,4,5,6]
length = len(a)
# indx表示的是list的下标
indx = 0
while indx < length:
    print(a[indx])
    indx += 1


# In[8]:

# 双层列表循环

# a是双层列表，或也叫嵌套列表
a = [['one',1],['two',2],['three',3]]
for k,v in a:
    print(k, '--', v)


# In[9]:

# 双层列表循环变异

#a 为嵌套列表，或者叫双层列表
a = [["one", 1, "eins"], ["two", 2], ["three", 3,4,5,6,8] ]

for k,v in a:
    print(k, "--", v)


# In[11]:

# 双层列表循环变异

#a 为嵌套列表，或者叫双层列表
a = [["one", 1, "eins"], ["two", 2,"zwei"], ["three", 3,"drei"] ]
#这个例子说明，k，v,w的个数应该跟解包出来的变量个数一致

for k,v,t in a:
    print(k, "--", v, '--',t )


# # 列表内涵: list content
# - 通过简单方法创建列表

# In[7]:

# for 创建
a = ['a', 'b', 'c']
# 用list a创建一个list b
# 下面代码的含义是，对于所有a中的元素，逐个放入新列表b中
b = [num for num in a]
print(b)
s = [275829]
s = (int)s
s.sort()
for i in s:
    print(i)


# In[15]:

# 对a中所有元素乘以10，生成一个新list
a = [1,2,3,4,5]
# 用list a创建一个list b
# 下面代码的含义是，对于所有a中的元素，逐个放入新列表b中
b = [num*10 for num in a]
print(b)


# In[16]:

# 还可以过滤原来list中的内容并放入新列表
# 比如原有列表a， 需要把所有a中的偶数生成新的列表b

a = [x for x in range(1,35)] #生成从1到34的一个列表
# 把a中所有偶数生成一个新的列表 b
b = [m for m in a if m % 2 == 0]
print(b)


# In[28]:

# 列表生成式可以嵌套
# 1.有两个列表a，b
print(1,'.')
a = [i for i in range(1,4)] # 生成list a
print(a)
print(2,'.')
b = [i for i in range(100,400) if i % 100 == 0]
print(b)

# 3.列表生成是可以嵌套,此时等于两个for循环嵌套
print(3,'.')
c = [  m+n for m in a for n in b]
print(c)

# 4.还可以写成下面这样：
print(4,'.')
for m in a:
    for n in b:
        print(m+n, end = ' ')
print( )
# 5.嵌套的列表生成式也可以用条件表达式
print(5,'.')
c = [m+n for m in a for n in b if (m+n)%2 == 0]
print(c)


# ## 列表的常用函数
# - len:求列表长度
# - max:求列表中的最大值
# - min：求列表中的最小值
# - list：将其他格式的数据转换成list
# - 把range产生的内容转换成list

# In[33]:

# len:求列表长度
a = [i for i in range(1,10)]
print(len(a))


# In[36]:

# max:求列表中的最大值
a = [m for m in range(3,10) if m %3 ==0]
print(max(a))
# min:求列表中的最小值
a = [m for m in range(3,10) if m %3 ==0]
print(min(a))


# In[38]:

# list：将其他格式的数据转换成list
m = 'ahaslimwliaiwr'
print(list(m))


# In[39]:

# 把range产生的内容转换成list
print(list(range(3,10)))


# In[2]:

# 传值和传地址的区别
# 对于简单的数值，采用传值操作，即在函数内对参数的操作不影响外面的变量
# 对于复杂变量，采用传地址操作，此时函数内的参数和外部变量是同一份内容，任何地方对此内容的更改都影响另外的变量或参数的使用

def a(n):
    n[2] = 300
    print(n)
    return None

def b(n):
    n += 100
    print(n)
    return None

num = [1,2,3,4,5]
t = 8

# 列表传址操作
print(num)
a(num)
print(num)

# 变量传值操作
print(t)
b(t)
print(t)


# ## 列表的其他函数
# - append: 插入一个内容, 在末尾追加
# - insert: 制定位置插入
# - del: 删除
# - pop: 从对位拿出一个元素，即把最后一个元素取出来
# - remove:在列表中删除指定的值的元素
# - clear:清空
# - reverse:翻转列表内容，原地翻转
# - extend:扩展列表，两个列表，把一个直接拼接到后一个上
# - count:查找列表中指定值或元素的个数
# - copy: 拷贝，此函数是浅拷贝

# In[8]:

l = [4,'fdkj','3dsf',32807,(23+5j)]
l


# In[17]:

# append 插入一个内容, 在末尾追加
a = [i for i in range(1,6)]
print(a)
a.append(99)
print(a)


# In[19]:

# insert: 制定位置插入
# insert(index, data), 插入位置是index前面
p = ['a','f','b',37,89]
p.insert(3,'love')
print(p)


# In[33]:

# del 删除
# pop 从对位拿出一个元素，即把最后一个元素取出来
a = [1,2,3,4,5,6]
del(a[0])
print(a)
# pop有返回值，返回最后一个元素值，并删除
b = a.pop()
print(b)
print(a)


# In[34]:

# remove:在列表中删除指定的值的元素
# 如果被删除的值没在list中，则报错
# 即，删除list指定值的操作应该使用try。。。excepty语句，或者先行进行判断
# if x in list:
#    list.remove(x)
print(a)
print(id(a))
a.remove(4)
print(id(a))
# 输出的id一样，说明list的remove操作是在原list里进行，没有生成一个新的list
# 删除的元素不在list里，则报错
# a.remove(10)
print(a)
if 8 in a:
    a.remove(8)
    print('ok')
else:
    print('fail')


# In[35]:

# clear:清空
print(a)
print(id(a))
a.clear()
print(id(a))
# 清空列表后id不变说明，clear是在原list里进行

# 如果不需要列表地址保持不变，则清空列表可以使用以下方式
# a = list()
# a = []


# In[38]:

# reverse:翻转列表内容，原地翻转
a = [1,2,3,4,5,6]
print(a)
print(id(a))
a.reverse()
print(id(a))
print(a)


# In[39]:

# extend:扩展列表，两个列表，把一个直接拼接到后一个上
a = [1,2,3,4,5,6]
b = [12,23,45,67]
print(id(a))
print(id(b))
a.extend(b)
print(a)
print(id(a))


# In[46]:

# count:查找列表中指定值或元素的个数
a = [11,23,11,1,11]
print(a.count(11))
a.append(11)
a.insert(2,11)
print(len(a))
print(a)
print(a.count(11))


# In[51]:

# 列表类型变量赋值示例
a = [1,2,3,4,5,666]
print('原a:',end = ' ')
print(a)
# list类型，简单赋值操作，是传地址
b = a
b[3] = 777
print('现a:',end = ' ')
print(a)
print('现a的id:',end = ' ')
print(id(a))
print('b:',end = ' ')
print(b)
print('b的id:',end = ' ')
print(id(b))

print("*" * 20)

# 为了解决以上问题，list赋值需要采用copy函数
b = a.copy()
b[3] = 129
print('现a:',end = ' ')
print(a)
print('现a的id:',end = ' ')
print(id(a))
print('b:',end = ' ')
print(b)
print('b的id:',end = ' ')
print(id(b))

print("*" * 20)


# In[52]:

# 深拷贝跟浅拷贝的区别
# 出现下列问题的原因是，copy‘函数是个浅拷贝函数，即只拷贝一层内容
# 深拷贝需要使用特定工具
a = [1,2,3, [10, 20, 30]]
b = a.copy()
print(id(a))
print(id(b))
print(id(a[3]))
print(id(b[3]))
a[3][2] = 666
print(a)
print(b)


# In[ ]:



