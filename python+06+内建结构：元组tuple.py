
# coding: utf-8

# # 元组- tuple
# - 元组可以看作一个不可更改的list

# ## 元组创建
# - 创建空元组
# - 创建一个只有一个值的元组
# - 创建多个值的元组
# - 使用其他结构创建

# In[1]:

# 创建空元组
t = ()
print(type(t))


# In[5]:

# 创建一个只有一个值的元组

t = (1)
# 只有一个值时，值后边要有，
a = (1,)
print(type(t))
print(t)
print(type(a))
print(a)

# 可以不带括号
b = 1,
print(type(b))
print(b)


# In[6]:

# 创建有多个值的元组
t = (1,2,3,4,5,)
print(type(t))
print(t)

# 可以不带括号
a = 1,2,3,4,5,
print(type(a))
print(a)


# In[8]:

# 使用其他结构创建元组
l = [1,2,3,4,5]
print(type(l))
l = tuple(l)
print(type(l))
print(l)


# ## 元组的特性
# - 是有序列表
# - 元组数据值可以访问，但不能修改
# - 元组数据可以是任意类型
# - 元组属于特殊列表，除了不能修改，list的其他属性元组都有
# - 也就是说，列表具有的操作：索引，分片，序列相乘，相加，成员资格等，元组全都具有

# In[18]:

# 索引操作
l = (1,2,3,4,6)
print(l)
print(type(l))


# In[24]:

# 分片操作
l = [1,2,3,4,5,6,7,8]
print(l[2::3])
print(l[:7:1])

# 切片可以超标
t = l[1:18]
print(t)


# In[30]:

# 序列相加,传址操作
t1 = [1,3,5]
t2 = [2,4,6]
print(id(t1))
t1 = t1 + t2
print(id(t1))
print(t1)

# 以上操作，类似于
t1 = (1,2,3)
t1 = (2,3,4)
# tuple 的不可修改，指的是内容的不可修改
# 修改tuple内容会导致报错
t1[1] = 100


# In[31]:

# 元组相乘
t = (1,2,4)
t * 3


# In[33]:

# 元组成员资格
t = (1,2,3,4,6)
print(1 in t)
print(7 not in t)


# In[34]:

# 元组遍历，一般采用for
# 1. 单层元组遍历
t = (1,2,3,"wangxiaojing", "i", "love")
for i in t:
    print(i, end=" ")


# In[35]:

# 2. 双层元组的遍历
t = ((1,2,3), (2,3,4),("i", "love", "wangxiaojing"))

# 对以上元组的遍历，可以如下
# 1.

for i in t:
    print(i)
    
for k,m,n in t:
    print(k,'--',m,'--',n)


# ## 关于元组的函数
# - 以下函数对于list基本适用
# - 函数如下：
#  - len ：获取元组长度
#  - min，max：获取元组元素最大值，最小值
#  - tuple：转化或创建元组
#  - count：计算指定数据出现的次数
#  - index：获取指定元素在元组中的位置

# In[1]:

# len ：获取元组长度
l = (1,2,3,4,5)
len(l)


# In[2]:

# min,max:求元组内元素最大值和最小值
a = min(l)
b = max(l)
print(a)
print(b)


# In[8]:

# tuple：转化或创建元组
l = [1,2,3,4,5]
t = tuple(l)
print(type(t))
print(t)

# 创建元组
t = tuple()
print(t)
print(type(t))


# In[10]:

# 求元组中指定元素出现次数
l = (1,2,3,4,5,6,4,4,4)
l.count(4)


# In[11]:

# 求指定元素索引
t = (1,2,3,4,5,6,7)
print(t.index(6))


# ### 元组变量交换法
# - 交换两个变量的值
# 

# In[21]:

# 定义两个变量，并输出各自的值
a = 10
b = 6
print(a)
print(b)
print('*' * 20)
# 交换变量的值
# java,C 程序员的写法
c = a
a = b
b = c
print(a)
print(b)
print('*'*20)
# python的写法
a,b = b,a
print(a)
print(b)


# In[ ]:



