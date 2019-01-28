
# coding: utf-8

# # 函数
# - 代码的组织形式
# - 一般一个函数完成一个特定功能
# - 函数使用：
#     - 函数需要先定义
#     - 使用函数，俗称调用
#     

# In[8]:

# 定义一个函数
# 只是定义不会执行
# 1.def关键字后跟一个空格
# 2.定义函数名，需要根据命名规则，不能用大驼峰命名法，它一般用于类
# 3.括号和冒号不能省，括号里可以有参数
# 4.函数内所有代码缩进
def func():
    print("这是一个函数")
    print("我的第一个Python函数")


# In[9]:

# 函数调用
# 直接函数名后跟括号
func()


# ### 函数的参数和返回值
# - 参数：负责给函数提供一些数据和信息
# - 返回值：函数执行后的返回结果
#     - 使用return关键字

# In[10]:

# 参数的定义和使用

def hello(name):
    print("你好啊，{0}".format(name))
    
p = "jinjin"
hello(p)


# In[24]:

# return语句的基本使用
# 如果没有返回值，系统默认返回None
# 一旦执行到return，函数无条件结束
# return案例1：
def hello(name):
    print("你好啊，{0}".format(name) )
    return '{0}已经跟我打过招呼了'.format(name)
    
p = "jinjin"
res = hello(p)
          
print(res)


# In[26]:

# return案例2
def hello(name):
    print("你好啊，{0}".format(name) )
    return '{0}已经跟我打过招呼了'.format(name)
    print("我结束了")
    return '拜拜'
p = "jinjin"
res = hello(p)
          
print(res)


# In[41]:

# 九九乘法表案例：
# version1.0
for row in range(1,10):
    # 打印一行
    for line in range(1,row+1):
        print(row * line,end = ' ')
    print('---------------------')
        


# In[50]:

# 定义一个函数 
def printRow(row):
    for line in range(1,row+1):
        print(row,end=' ')
        print('*',end=' ')
        print(line,end=' ')
        print('=',end=' ')
        print(row * line,end=' ')
    print(' ')
# 九九乘法表案例：
# version2.0
for row in range(1,10):
    printRow(row)
        


# ## 参数详解
# - 参考资料[http://www.cnblogs.com/bingabcd/p/6671368.html]
# - python参考资料：headfirst Python->零基础入门学习Python（小甲鱼）->习题，后期可以参考腾讯公开课
# - 参数分类：
#     - 普通参数
#     - 默认参数
#     - 关键字参数
#     - 收集参数
# - 普通参数：
#     - 定义的时候直接定义变量名
#     - 调用的时候直接把变量或值放在指定位置
#     
#         def 函数名(参数1，参数2，参数3):
#             函数体
#             
#         #调用
#         
#         def 函数名(value1,value2,value3)
#         
#  - 默认参数：
#      - 形参带有默认值
#      - 调用的时候如果没有对形参赋值，则直接使用默认值
#      
#      def 函数名(p1=v1,p2=v2,...):
#          函数体
#          
#       #调用
#       函数名（）
#       
#       #调用2 
#       value1 = 100
#       value2 = 200
#       函数名（value1，value2）
# 

# In[54]:

# 默认参数实例：
# 报名函数，报名需要知道性别
# 默认为男生，如果是男生，就不用说了，女生的话说一声
def baoMing(name,age,gender='male'):
    if(gender=='male'):
        print('{0} is {1} years old,he is a {2}'.format(name,age,gender))
    else:
        print('{0} is {1} years old,she is a {2}'.format(name,age,gender))


# In[57]:

# 调用默认参数实例：
baoMing('小小',18)
baoMing('jingjing',20,'female')


# ## 关键字参数
# - 语法
# 
#       def func（p1=v1，p2=v2....）:
#       func_body
#       
#       调用函数：
#       func（p1=value1，p2=value2....）
# - 比较麻烦，但也有好处
#     - 不容易混淆，一般实参和形参要一一对应即可，容易出错
#     - 使用关键字参数，不用考虑参数位置

# In[1]:

# 关键字参数实例：
def stu(name,age,addr):
    print('我是一个学生')
    print('我叫{0}，我今年{1}岁，家住在 {2}'.format(name,age,addr))
stu('小小',18,'宋村')


# In[2]:

# 使用关键字参数，可以调换参数位置，不会引发错误
def stu_key(name='no name',age=18,addr='no addr'):
    print('我是一个学生')
    print('我叫{0}，我今年{1}岁，家住在 {2}'.format(name,age,addr))
stu_key(name='小小',addr='宋村',age=18)


# ## 收集参数
# - 把没有位置，不能和定义时一一对应位置的参数放进一个特定的数据类型
# - 语法
# 
#     def func(*args):
#         func_body
#         
#     调用函数：
#     func(p1,p2,p3....)
#     - 按照list的调用方法得到从args传来的参数
#     - 参数名args不是必须这么写，但推荐这么写，约定俗成
#     - args前用*
#     - 收集参数可以和其他参数并存

# In[5]:

# 收集参数代码实例：
# 函数模拟一个学生做自我介绍，但具体介绍内容不清楚
def stu(*args):
    print('大家好，请允许我做个自我介绍：')
    #打印出args的类型
    print(type(args))
    for item in args:
        print(item)
    
stu('lily',18,'WuTong')
stu('jie')


# In[6]:

# 收集参数实例2：
# 收集参数可以不带任何实参调用，这时收集参数是一个空tuple
stu()


# ## 收集参数之关键字收集参数
# - 将关键字参数按字典格式存入收集参数
# - 语法
#         def func（**kwargs）:
#             func_body
#             
#         - 调用函数：
#         func（p1=v1, p2=v2.....）
#         - kwargs一般约定俗成，也可以用其他的
#         - 可以把多余的关键字参数放进kwargs
#         - 访问kwargs按照访问字典的格式

# In[16]:

### 收集参数案例：
# 自我介绍
# 调用时需要使用关键字参数调用
def stu(**kwargs):
    print('大家好，先来个自我介绍')
    print(type(kwargs))
    # 对于字典的调用，Python2和Python3有不同
    #下面是字典的调用格式
    for k,v in kwargs.items():
        print(k,'---',v)
    
    print('*'* 20)

stu(name='zhoudafu',age=18,addr='no addr')
stu(name='me')    


# In[17]:

# 收集参数可以为空案例
stu()


# ### 收集参数混合调用的顺序问题
# - 收集参数，普通参数，关键字参数可以混合使用
# - 使用规则是：普通参数和关键字参数优先
# - 定义的时候先找普通参数，然后是关键字参数，再有收集参数tuple,收集参数dict

# In[30]:

# 混合调用例子
#模拟自我介绍
def stu(name, age,  *args, hobby='',**kwargs):
    print('hello,大家好')
    print('我叫{0},我今年{1}岁了。'.format(name,age))
    if(hobby==''):
        print('sorry,我没有爱好')
    else:
        print('我的爱好是：{0}'.format(hobby))
    for i in args:
        print(i)
    for k,v in kwargs.items():
        print(k,'----',v)
    print('*'*20)
        
name = 'xiaoxiao'
age = 18
#调用函数：
stu(name,age)
stu(name,age,hobby='play')
stu(name,age,'kadfh',hobby='play',addr='hsk',hobby2='go hiking')
# 参数种类比较多时，收集参数往前提，关键字参数往后放


# ### 收集参数的解包问题
# - 直接将参数放进list或字典里，将list或字典里的值放进收集参数里
# - 语法：参见案例

# In[44]:

#收集参数的解包问题案例；
def stu( *args):
    print('hahhahahha')
    n = 0
    for i in args:
        print(n)
        print(i)
        n += 1
        
l = ['xiaoxiao',18,'nihaomei']
stu(l)
# 此时，args里的表现形式是一个list类型的元素
# 很显然，跟我们的想法不同


# 此时的调用我们就需要解包符号，即在前面加一个*
stu(*l)


# ### 同理，dict的调用同样也需要解包
# - 不过需要两个星号

# # 返回值
# - 函数与过程的区别
#     - 有无返回值
# - 需要用return显示返回内容
# - 如果没有返回，则默认返回None
# - 推荐写法，无论有无返回值，左后都已return结尾

# In[35]:

# 返回值实例：
def fun1():
    print('我有返回值')
    return 1

def fun2():
    print('我没有返回值')
    
f1 = fun1()
print(f1)
f2 = fun2()
print(f2)


# # 函数文档
# - 函数的文档的作用是对当前函数使用相关的参考信息
# - 文档的写法：
#     - 在函数内部开始的第一行使用三字符串定义符
#     - 一般具有特定格式
#     - 参考案例
# - 文档查看
#     - 使用help函数，形如help（stu）
#     - 使用__doc__,参看案例

# In[3]:

# 文档案例
# 函数自我介绍
def stu(name, age, *args):
    '''
    第一行
    第二行
    第三行
    '''
    print('这是函数')


# In[5]:

help(stu)
stu.__doc__


# In[6]:

# 文档注释实例：
def stu(name, age):
    '''
    这是文档的文字内容
    :param name: 表示学生的姓名
    :param age: 表示学生的年龄
    :return: 此函数没有返回值
    '''
    pass


print(help(stu))

print("*" * 20)

print(stu.__doc__)


# # 变量作用域
# - 变量由作用范围限制
# - 分类：按照作用域分类：
#     - 全局（global）：在函数外部定义
#     - 局部（local）:在函数内部定义
# - 变量的作用范围：
#     - 全局变量：在整个全局范围都有效
#     - 全局变量在局部可以使用(即函数内部可以访问外部定义的变量)
#     - 局部变量在局部范围可以使用
#     - 局部变量在全局范围无法使用
# - LEGB原则
#     - L（local）局部作用域
#     - E（Enclosing function locale）外部嵌套函数作用域
#     - G（Global module）函数定义所在模块作用域
#     - B（Buildin）python内置魔抗的作用域

# ## 提升局部变量为全局变量
# - 使用global
# - 案例如下：

# In[18]:

def fun():
    global b1
    b1 = 100
    print(b1)
    print('i am in fun')
    b2 = 99
    print(b2)
fun()   
print(b1) # 如果在函数调用上面，则出错，为什么？？
#print(b2)


# # golbals,locals函数
# - 可以通过globals和locals显示出局部变量和全局变量
# - 参看以下案例

# In[11]:

# glocals和locals
a = 1
b = 1
def fun(c,d):
    e = 111
    print('locals={0}'.format(locals()))
    print('Globals={0}'.format(globals()))
    
fun(a,b)


# # eval()函数
# - 是一个字符串当做一个表达式来执行，返回表达式执行的结果
# - 语法：
# 
#         eval(string_code,globals=None,locals=None)
# # exec()函数
# - 跟eval函数功能一样，但是不返回结果
# - 语法：
# 
#         exec(string_code,globals=None,locals=None)

# In[12]:

# eval()函数实例：
x = 100
y = 200
#执行x+y
# z = x + y
z1 = x + y
z2 = eval('x+y')

print(z1)
print(z2)


# In[15]:

# exec函数实例：
x = 100
y = 200
#执行x+y
# z = x + y
z1 = x + y
# 1.注意字符串中引号的写法
# 2.对比exec执行结果和代码执行结果
z2 = exec("print('x+y:',x+y)") # 首先执行

print(z1)
print(z2)


# # 递归函数
# - 函数直接间接调用调用自身
# - 优点：简洁，理解容易
# - 缺点：对递归深度有限制，消耗资源大
# - Python对递归深度有限制，超过限制会报错

# In[19]:

# 递归调用深度限制代码：
x = 0
def fun():
    global x
    x += 1
    print(x)
    # 函数自己调用自己
    fun()
    
# 调用函数
fun()


# ## 斐波那契数列：
# - 规则：
#  - 一列数字，第一个值是1，第二个值也是1，从第三个数起，每一个数字等于前两个数字之和
#  - 数学公式为:f(1) = 1, f(2) = f(0) + f(1) ,f(n) = f(n-1) + f（n-2）
#  - 例如： 1,1,2,3,5,8,13.。。。。

# In[ ]:

# n表示第n个数字的斐波那契数列的值
def fb(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    
    return fb(n-2) + fb(n-1)
print(fb(3))
print(fb(10))


# 

# ## 汉诺塔问题
# - 规则：
#     - 1.每次只能移动一个盘子
#     - 2.移动时必须保证大盘子在上，小盘子在下
# - 方法：
#     1. n=1： 直接把A上的一个盘子移动到C上， A->C
#     2. n=2: 
#         1. 把小盘子从A放到B上， A->B
#         2. 把大盘子从A放到C上， A->C
#         3. 把小盘子从B放到C上， B->C
#     3. n=3: 
#         1. 把A上的两个盘子，通过C移动到B上去， 调用递归实现
#         2. 把A上剩下的一个最大盘子移动到C上， A->C
#         3. 把B上两个盘子，借助于A，挪到C上去， 调用递归
#     4. n = n：
#         1. 把A上的n-1个盘子，借助于C，移动到B上去，调用递归
#         2. 把A上的最大盘子，也是唯一一个，移动到C上，A->C
#         3. 把B上n-1个盘子，借助于A，移动到C上， 调用递归
# 

# In[12]:

# 代码：
def hano(n,a,b,c):
     '''
    汉诺塔的递归实现
    n：代表几个盘子
    a：代表第一个塔，开始的塔
    b：代表第二个塔，中间过渡的塔
    c：代表第三个塔, 目标塔
    '''
    if n == 1:
        print(a , '->' ,c)
        return None
    # 可以把n==2省略
    if n == 2:
        print(a , '->' , b)
        print(a , '->' , c)
        print(b , '->' , c)
        return None
    # 当n比较大时，思路是：
    # 先将n-1个盘子借助于c移动到b上，再将a上剩余的1个盘子移动到c上，再将n-1个盘子借助a移动到c上
    hano(n-1,a,c,b)
    print(a , '->' , c)
    hano(n-1,b,a,c)


# In[18]:

a = 'A'
b = 'B'
c = 'C'
n = 5

hano(n,a,b,c)


# In[ ]:



