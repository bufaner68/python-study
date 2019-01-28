
# coding: utf-8

# # dict 字典
# - 字典是一种组合数据，没有顺序的组合数据，数据以一种键值对的形式存在

# In[11]:

# 字典的创建
# 创建空字典1
d = {}
print(type(d))
# 创建空字典2
d1 = dict()
print(type(d1))

# 创建有值的字典， 每一组数据用冒号隔开， 每一对键值对用逗号隔开
d2 = {1:'one',2:'two',3:'three'}
for k,v in d2.items():
    print(k,'-',v)
print('*'*20)
# 用dict创建有内容字典1
d3 = dict({1:'one',2:'two',3:'three'})
print(d3)

print('*'*20)
# 用dict创建有内容字典2
# 利用关键字参数
d4 = dict(one=1, two=2, three=3)
print(d4)

#
print('*'*20)
d = dict( [("one",1), ("two",2), ("three",3)])
print(d)


# # 字典的特征
# - 字典是序列类型，但是是无序序列，所以没有分片和索引
# - 字典中的数据每个都有键值对组成，即kv对
#     - key: 必须是可哈希的值，比如int,string,float,tuple, 但是，list,set,dict 不行
#     - value: 任何值

# ## 字典的常见操作
# - 访问数据
# - 删除某个操作
# - 使用del操作
# - 成员检测： in， not in
# - 元素遍历

# In[13]:

# 访问数据
d =  {1:'one',2:'two',3:'three'}
# 注意访问格式
# 中括号内是键名
print(d[1])

d[1] = "eins"
print(d)


# In[21]:

# 删除某个操作
# 使用del操作
d =  {1:'one',2:'two',3:'three'}
del d[1]
print(d)
del(d)


# In[22]:

# 成员检测， in， not in
# 成员检测检测的是key内容
d = {"one":1, "two":2, "three":3}

if 2 in d:
    print("value")
    
if "two" in d:
    print("key")
    
if ("two",2) in d:
    print("kv")


# In[26]:

# 便利在python2 和 3 中区别比较大，代码不通用
# 按key来使用for循环
d = {"one":1, "two":2, "three":3}
# 使用for循环，直接按key值访问
for k in d:
    print(k,d[k])
    
# 上述代码可以改写成如下
for k in d.keys():
    print(k,d[k])

# 只访问字典的值
for v in d.values():
    print(v)
    
# 注意以下特殊用法
for k,v in d.items():
    print(k,'--',v)


# ## 字典生成式

# In[37]:

d = {'i':'我','love':'爱','u':'你'}
print(d)
# 常规字典生成式
dd = {k:v for k,v in d.items()}
print(dd)
# 加限制条件的字典生成式
ddd = {k:v for k,v in d.items() if k == 'u'}
print(ddd)


# ## 字典相关函数
# - 通用函数： len, max, min, dict
# - str(字典): 返回字典的字符串格式
# - clear: 清空字典
# - items: 返回字典的键值对组成的元组格式
# - keys:返回字典的键组成的一个结构
# - values: 同理，一个可迭代的结构
# - get: 根据制定键返回相应的值， 好处是，可以设置默认值
# - fromkeys: 使用指定的序列作为键，使用一个值作为字典的所有的键的值

# In[41]:

# str(字典): 返回字典的字符串格式
d = {1:'one',2:'two',3:'three'}
print(str(d))
print(d)


# In[42]:

# clear: 清空字典
# items: 返回字典的键值对组成的元组格式

d = {"one":1, "two":2, "three":3}
i = d.items()
print(type(i))
print(i)


# In[43]:

# keys:返回字典的键组成的一个结构
k = d.keys()
print(type(k))
print(k)


# In[44]:

# values: 同理，一个可迭代的结构
v = d.values()
print(type(v))
print(v)


# In[45]:

# get: 根据指定键返回相应的值， 好处是，可以设置默认值

d = {"one":1, "two":2, "three":3}
print(d.get("on333"))

# get默认值是None，可以设置
print(d.get("one", 100))
print(d.get("one333", 100))

#体会以下代码跟上面代码的区别
print(d['on333'])


# In[46]:

# fromkeys: 使用指定的序列作为键，使用一个值作为字典的所有的键的值
l = ["eins", "zwei", "drei"]
# 注意fromkeys两个参数的类型
# 注意fromkeys的调用主体
d = dict.fromkeys(l, "hahahahahah")
print(d)


# In[ ]:



