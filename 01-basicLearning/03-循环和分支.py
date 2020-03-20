"""
1.import导入，和java一样
2.循环和分支语句后面一定记得:，没有冒号ide都不会自动添加tab。并且没有()
3.if elif else
4.三目运算符 a if a>b else b
5.for item in arr for循环
"""
import random

print(1 if False else 2)

print('-----游戏开始----')
num = int(input('请输入一个数字:'))
targetNum = random.randint(1, 100)
while num != targetNum:
    if num > targetNum:
        print('数字太大，重新输入')
    elif num < targetNum:
        print('数字太小，重新输入')
    num = int(input('请重新输入一个数字:'))
print('答对了----')
