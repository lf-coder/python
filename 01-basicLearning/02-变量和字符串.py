"""
1.定义变量不需要声明，变量是没有类型的
2.使用tab替代类似java的{}，使代码更简洁，但是得小心使用
3.字符串和js差不多使用""或''
"""

print('----游戏开始----')
temp = input('请输入一个数字:')
num = int(temp)
if num == 8:
    print('猜对了')
else:
    print('答错了')
print('游戏结束')

