
# coding: utf-8

# # while循环
# - 一个循环语句
# - 当条件表达式成立时，执行循环
# - 不确定具体循环次数，当能确定循环条件时使用
# - while语法：
#      
#      while 条件表达式:
#          语句1
#          语句2
#          .....
# # 另一种表达方式
#      
#      while 条件表达式：
#          语句块
#      else：
#          语句块

# In[7]:

# 案例1：
# 如果年利率是6.7%，本利是每年翻滚，求多少年本钱会翻倍
benqian = 100000
year = 0
while benqian < 200000:
    benqian = benqian*1.067
    year = year + 1
    print ('{0}年后本钱是{1}'.format(year,benqian))
    


# In[9]:

# 案例2：
# 如果年利率是6.7%，本利是每年翻滚，求多少年本钱会翻倍
benqian = 100000
year = 0
while benqian < 200000:
    benqian = benqian*1.067
    year = year + 1
    print ('{0}年后本钱是{1}'.format(year,benqian))
else:
    print("终于翻倍了")

