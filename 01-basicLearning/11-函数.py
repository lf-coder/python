"""
1.函数的参数：形参和实参、关键字参数、默认参数和可变参数
2.python中的函数和js中的函数一样，可以当作数据类型传递；可以在函数中嵌套函数
3.函数中可以使用global关键字声明全局变量
4.内部函数不能修改我外部函数的局部变量，需要使用nonlocal实现
5.lambda表达式：lambda x:x*=x。python中的lambda追求简单、精简，在语法上，他们也会被严格限制为一个单表达式。
"""


# 1-1 关键字参数
def fun1(name, age):
    print(name + '=>' + str(age))


fun1('lf', 23)

# 1-2 默认参数
fun1(age=23, name='lf')


# 可变参数  前面有可变参数，如果最后一个参数不是可变参数，请使用默认参数，调用使用关键字参数
def fun2(*param, some='hhh'):
    print(param[0])
    print(len(param))
    print(some)


fun2('lf', 23, some='xxx')


# 函数当作参数传递
def fun3(fun):
    fun('lf', 23)


fun3(fun1)


# 声明全局变量，必须要运行函数才能在外面使用函数内部定义的全局变量
def fun4():
    global global1
    global1 = 20


fun4()
print(global1)


# nonlocal使用
def fun5():
    x = 5

    def fun5_1():
        nonlocal x  # 先要使用nonlocal修饰
        x *= 2  # 直接修改值会出错
        print(x)

    fun5_1()


fun5()

# lambda
fun6 = lambda x: x * 2
print(fun6(2))

