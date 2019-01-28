
# coding: utf-8

# # 程序结构
#    - 顺序
#    - 分支
#    - 循环

# # 分支
#  - 分支的语法结构：
#         
#         if 条件表达式：
#            语句1
#            语句2
#            语句3
#            ......
#    - 条件表达式后面的冒号不能少
#    - 注意条件表达式后边的语句，如果为if语句块，则必须同一个缩进等级
#   

# In[12]:

# if语句实例
# 年龄小于18，打印叫家长去
age = 19
if age < 18:
    print("叫家长去")
    print("不能带你玩")
    print("走吧")
print("一起玩吧")


# ### 双向分支
#     - if....elae
#     
#         if 条件表达式：
#             语句1
#             语句2
#             ......
#         else:
#             语句1
#             语句2
#             ......
#             
#         - 缩进问题，if，else一个层级，其余语句一个层级

# In[23]:

# input语句的作用是：在屏幕上输出括号里的字符串
# 接收用户在屏幕上输入的字符串并返回程序
#input返回的内容一定是字符串
# 范例1
gender = input("请输入性别：")
print("您输入的性别是%s"%(gender))
if gender == "nv":
    print("女神节快乐")
else:
    print("男生祝女神女生节快乐")
print("敲代码咯")


# In[43]:

# 范例2
# 考试成绩，60-70：及格，70-80：中等，80-90：良好，90以上：优秀，小于60：不及格
# 注意input返回值类型
# 需要把str转换成int
score = input("请输入成绩：")
print("您的成绩是%s"%(score))
score = int(score)
if score < 60:
    print("不及格")
else:
    if 70 > score >= 60:
        print("及格")
    else:
        if 80 > score >= 70:
            print("中等")
        else:
            if 90 > score >= 80:
                print("良好")
            else:
                if 100 >= score >= 90:
                    print("优秀")
                


# # 多路分支
#   - 很多分支的情况，简称多路分支
#         if 条件表达式：
#             语句1
#             ......
#         elif 条件表达式：
#             语句1
#             ......
#         elif 条件表达式：
#             语句1
#             ......
#         elif 条件表达式：
#             语句1
#             ......
#         else:
#             语句1
#             ......
#     - elif可以有很多个
#     - else可选
#     - 多路分支只选择执行一条语句

# In[48]:

# 案例
score = input("请输入成绩：")
print("您的成绩是%s"%(score))
score = int(score)
if score < 60:
    print("不及格")
elif 70 > score:
    print("及格")
elif 80 > score:
    print("中等")
elif 90 > score:
    print("良好")
else:
    print("优秀")
                 


# ## if语句其他
# - 可以嵌套，但不推荐
# - Python里没有switch...case

# # 循环语句
# - for循环
# - while循环
# ## for循环
# - for循环语法：
# 
#       for 变量 in 序列:
#        语句1
#        ....
#        

# In[55]:

# 序列就是一列数字或其他，用中括号括起来
# 打印学生列表姓名
for name in ['lily','lucy','tom','jack']:
    print(name)


# In[59]:

# 打印学生列表姓名
# 如果是Jack，温柔对待
for name in ['lily','lucy','tom','jack']:
    print(name)
    if name=='jack':
        print("你好帅{0}".format(name))
    else:
        print("走开")


# ## range序列
# - 生成一个数字序列
# - 具体范围可以设定

# In[64]:

# range练习
# 打印从1到10的数字
# 注意，Python里，如果有两个表示数字范围的两个数字，一般包含左边，不包含右边
# rangeint是特例，左右都包含
# range函数在Python2 和Python3 有严重区别
for i in range(1,11):
    print(i)


# ## for-else语句
# - 当for循环结束的时候，会执行else语句
# - else语句是可选语句

# In[68]:

# for-else语句案例
# 打印列表里的同学
# 如果没有在列表中，或者打印结束了，打印出提示语句
for name in ['lily','lucy','tom','jack']:
    print(name)
    if name=='jack':
        print("我的爱豆{0}".format(name))
    else:
        print("走开")
else:
    print("结束了")


# In[ ]:

# for循环之break，continue，pass
- break：一旦执行到这里，立即无条件结束整个循环
- continue：立即无条件结束本次循环
- pass：表示略过


# In[74]:

# break案例：
# 在1到10里，寻找7，一旦找到，打印，否则什么也不做
# 在for循环中，一般用i,k,m,n或者indx,idx,item之类
# 在Python中，如果变量名不重要，可以用_代替
for i in range(1,11):
    if i==7:
        print("找到了")
        break
    else:
        print(i)


# In[77]:

# continue案例：
# 在1到10里，寻找所有偶数，找到了就打印，否则什么也不做
for i in range(1,11):
    if i % 2 == 0:
        print('{0}是偶数'.format(i))
    


# In[79]:

# continue案例版本2：
# 在1到10里，寻找所有偶数，找到了就打印，否则什么也不做
# 本案例完美展示continue的用法
for i in range(1,11):
    if i % 2 == 1:
        continue
        
    print('{0}是偶数'.format(i))


# In[84]:

# pass案例，pass表示占位
for i in range(1,11):
    pass
    print('我在')

