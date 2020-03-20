"""
1.元组可以看做一种不可以改变元素的数组。不能进行添加和删除操作
2.创建元组逗号是关键，小括号不是关键，小括号可以省略
3.元组也可以使用+、*、in\not in
"""

"""创建一个元组"""
print(())
"""这不是元组 (1)等价于1"""
print((type((1))))
print((1,))
temp = 1,
print(temp)

"""元组操作"""
tuple = 1, 2, 3, 4
print(tuple)
print(tuple[0])
print(tuple[1:3])
print(2 * tuple)
print(tuple + (2, 3))
print(2 in tuple)

"""分片操作可以达到修改元组元素的目的"""
print(tuple[:2] + (1.2,) + tuple[2:])
print(tuple[:2] + tuple[3:])
