"""
1.python中的数组和js中的数组一样，作用和java的链表差不多
2.方法：append、extend、insert
3.删除：arr.remove(元素)、del 数组/数组[index] 、arr.pop()
4.分片：arr[index1:index2] 前闭后开，返回原数组的浅拷贝
5.+号可以连接两个数组、*可以将数组元素复制、in和not in可以判断元素是否在数组中
6.dir可以查看对象的结构
"""
arr = ['hello', 'world', 12, ['1', '2']]
print(arr)

arr.append('hello world')
print(arr)

arr.extend(['lf', 23])
print(arr)

arr.insert(0, 'first')
print(arr)

print(len(arr))

del arr[2]
print(arr)

print(arr[1:3])
print(arr[:3])
print(arr[1:])
print(arr[:])

print([1, 2] in [[1, 2], 3, 4])

print(dir(arr))

arr1 = [1, 2]
arr2 = [arr1, 3, 4]
arr3 = arr2[:]
arr1.append(5)
print(arr2)
print(arr3)
