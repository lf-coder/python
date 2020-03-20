# 求n的阶乘
def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n - 1)


print(factorial(5))


# 斐波拉契数列，一月份有一对兔子，每个2个月就会产下一对兔子，产下的一对兔子每隔两个月又产下一对兔子，以此类推
# 并不是所有的程序都使用递归，比如这个例子当月份越大，迭代的效率就比递归高
def fibonacci(month):
    if month in [1, 2]:
        return 1
    else:
        return fibonacci(month - 2) + fibonacci(month - 1)


print(fibonacci(9))
