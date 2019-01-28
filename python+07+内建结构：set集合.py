
# coding: utf-8

# # 集合set
# - 集合是高中数学里的一个概念

# In[1]:

# 集合的定义
s = set()
print(type(s))
print(s)

# 此时，大括号内一定要有值，否则定义出的是一个dict
s = {1,2,3,4,5,6,7}
print(s)


# In[2]:

# 如果只是用大括号定义，则定义的是一个dict类型
d = {}
print(type(d))
print(d)


# ## 集合的特征
# - 集合内的元素是无序的，即无法使用索引和分片
# - 集合内的元素是唯一的，可以用来排除重复元素
# - 集合内的元素，str,int,float,tuple,冰冻集合等，即只能存放可哈希数据

# ### 集合序列的操作
# - 成员资格检查
#  - in，not in
# - 集合遍历操作
#  - for循环

# In[7]:

# 资格检查：in，not in
s = set()
s = {1,2,3,4,5,6}
print(5 in s)
if 9 not in s:
    print('9 not in s')


# In[10]:

# 集合的遍历
s = {12,3,6,9,8}
for i in s:
    print(i,end = ' ')


# In[13]:

# 带有元组的集合遍历
s = {(1,2,3),('i','like','u'),('ha','ha','ha')}
for m,n,k in s:
    print(m,'-',n,'-',k)
print('*'* 20)
for v in s:
    print(v)


# ## 集合的内涵
# - 普通集合内涵
# - 带条件集合内涵
# - 多循环的集合内涵

# In[14]:

# 普通集合内涵
# 以下集合在初始化后自动过滤掉重复元素
s = {23,223,545,3,1,2,3,4,3,2,3,1,2,4,3}
print(s)

# 普通集合内涵
ss = {i for i in s}
print(ss)


# In[16]:

# 带条件的集合内涵
sss = {m for m in s if m%3 ==0}
print(sss)


# In[20]:

# 多循环的集合内涵
s1 = {1,2,3,4}
s2 = {"i", "love", "u"}
s = {m * n for m in s1 for n in s2}
print(s)
s = {m * n for m in s1 for n in s2 if m ==1}
print(s)


# ## 关于集合的函数
# - 集合的一般函数：
#     - len，max，min与其他的 一样
#     - set：生成一个集合
#     - add：向集合添加一个元素
#     - clear：原地清空集合
#     - copy: 拷贝
#     - remove: 移除制定的值，直接改变原有值，如果要删除的值不存在，报错
#     - discard: 移除集合中指定的值
#     - pop ：随机移除一个元素
# - 集合的特有函数：
#     - intersection: 交集
#     - difference:差集
#     - union: 并集
#     - issubset: 检查一个集合是否为另一个子集
#     - issuperset: 检查一个集合是否为另一个超集

# In[22]:

# len, max, min:跟其他基本函数一致
s = {43,23,56,223,4,2,1222,4,323,1}
print(len(s))
print( max(s))
print(min(s))


# In[23]:

# set:转化或生成一个集合
l = [1,2,3,4,3,23,1,2,3,4]
s = set(l)
print(s)


# In[24]:

# 向集合添加啊一个新的元素
s.add(99)
print(s)


# In[26]:

#clear
s = {1,2,3,4,5}
print(id(s))
s.clear()
print(id(s))
print(s)
# 结果表明ｃｌｅａｒ函数是原地清空数据


# In[27]:

# copy:拷贝
# remove:移除制定的值，直接改变原有值，如果要删除的值不存在，报错
# discard:移除集合中指定的值，跟ｒｅｍｖｏｅ一样，但是如果要删除的话，不报错
s = {23,3,4,5,1,2,3}
s.remove(4)
print(s)
s.discard(1)
print(s)

print("*" * 20)
s.discard(1100)
print(s)

s.remove(1100)
print(s)

# 为啥ｒｅｍｏｖｅ不存在的值会报ｋｅｙｅｒｒｏｒ


# In[28]:

# pop 随机移除一个元素
s = {1,2,3,4,5,6,7}
d = s.pop()
print(d)
print(s)


# In[31]:

# 集合函数
# intersection: 交集
# difference:差集
# union: 并集
# issubset: 检查一个集合是否为另一个子集
# issuperset: 检查一个集合是否为另一个超集
s1 = {1,2,3,4,5,6}
s2 = {5,6,7,8,9}

s_1 = s1.intersection(s2)
print(s_1)

s_2 = s1.difference(s2)
print(s_2)

s_3 = s1.issubset(s2)
print(s_3)


# In[34]:

# 集合的数学操作
s1 = {1,2,3,4,5,6}
s2 = {6,7,8,9}

s_1 = s1 - s2
print(s_1)

s_2 = s1 + s2
print(s_2)


# ## frozenset:冰冻集合
# - 冰冻集合就是不能进行任何修改的集合
# - 冰冻集合是一种特殊的集合

# In[36]:

s = frozenset()
print(type(s))
print(s)


# In[ ]:



