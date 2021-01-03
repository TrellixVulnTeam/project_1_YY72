# '''
# 求和
# '''
# sum = 0
# for x in range(0,101,2):
#     sum += x
# print(sum)

# '''
# 猜数字
# '''
# import random
#
# answer = random.randint(1, 100)
# counter = 0
# while True:
#     counter += 1
#     number = int(input('请输入: '))
#     if number < answer:
#         print('大一点')
#     elif number > answer:
#         print('小一点')
#     else:
#         print('恭喜你猜对了!')
#         break
# print('你总共猜了%d次' % counter)
# if counter > 7:
#     print('你的智商余额明显不足')

# '''
# 最大公约数和最小公倍数
# '''
#
#
# def gcd(x, y):
#     if x < y:
#         x, y = y, x
#     if y != 0:
#         公约数 = gcd(x % y, y)
#         return 公约数
#     else:
#         return x
#
#
# x = int(input('x='))
# y = int(input('y='))
# print(gcd(x, y), x * y / gcd(x, y))
