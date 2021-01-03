# '''
# 变量
# '''
# a = 321
# b = 12
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)

# '''
# 检查变量类型
# '''
# a = 100
# b = 12.345
# c = 1 + 5j
# d = 'hello,world'
# e = True
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
# print(type(e))
# # <class 'int'>
# # <class 'float'>
# # <class 'complex'>
# # <class 'str'>
# # <class 'bool'>

# '''
# input 获取键盘输入(字符串)
# int 转换成整形
# print 输出
# '''
# a = int(input('a = '))
# b = int(input('b = '))
# print('%d+%d=%d' % (a, b, a + b))
# print(f'{a}-{b}={a - b}')
# print('%d*%d=%d' % (a, b, a * b))
# print('%d/%d=%f' % (a, b, a / b))
# print('%d//%d=%d' % (a, b, a // b))
# print('%d %% %d=%d' % (a, b, a % b))
# print('%d ** %d = %d' % (a, b, a ** b))

# '''
# 赋值运算符
# '''
# a = 10
# b = 3
# a += b
# a *= a + 2
# print(a)

# '''
# 比较运算符
# '''
# flag0 = 1 == 1
# flag1 = 3 > 2
# flag2 = 2 < 1
# flag3 = flag1 and flag2
# flag4 = flag2 or flag1
# flag5 = not (1 != 2)
# print('flag0 =', flag0)  # flag0 = True
# print('flag1 =', flag1)  # flag1 = True
# print('flag2 =', flag2)  # flag2 = False
# print('flag3 =', flag3)  # flag3 = False
# print('flag4 =', flag4)  # flag4 = True
# print('flag5 =', flag5)  # flag5 = False

'''
华氏温度转换
'''

f=float(input('温度='))
c=(f-32)/1.8
print(f'{c:.1f}°C')
