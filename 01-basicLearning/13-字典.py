"""
1.字典是dict的实例
1.python的字典和js中的对象一模一样
2.可以使用in 和 not in判断字典中是否有该key
"""

# 创建一个字典
dict1 = {'name': 'lf', 'age': 23}
print(dict1)

dict2 = dict((('name', 'lf'), ('age', 23)))
print(dict2)

dict3 = dict(name='lf', age=23)
print(dict3)
dict3['hobby'] = 'play game'
print(dict3)
