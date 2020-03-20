"""
1.字符串的格式化有两种方式
2.str.format(s1,s2,s3)  str.format(key1=value1,key2=value2,key3=value3)
3.str % (s1,s2,s3)
"""

print('{0}的名字叫{1}'.format('我', 'lf'))
print('{who}的名字叫{name}'.format(who='我', name='lf'))
print('%s的名字叫%s' % ('我', 'lf'))
print('这个数字被四舍五入了:{0:.1f}'.format(25.36))