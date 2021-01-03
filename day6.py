# m = int(input('m = '))
# n = int(input('n = '))
# fm = 1
# for num in range(1, m + 1):
#     fm *= num
# fn = 1
# for num in range(1, n + 1):
#     fn *= num
# fm_n = 1
# for num in range(1, m - n + 1):
#     fm_n *= num
# print(fm // fn // fm_n)

# def add(*args):
#     sum = 0
#     for val in args:
#         sum += val
#     return sum
#
# print(add(1,2,3,4,5,6,7))
# print(add(1,2,3,4,5))

# def foo():
#     b = 'hello'
#
#     # Python中可以在函数内部再定义函数
#     def bar():
#         c = True
#         print(a)
#         print(b)
#         print(c)
#
#     bar()
#     # print(c)  # NameError: name 'c' is not defined
#
#
# if __name__ == '__main__':
#     a = 100
#     # print(b)  # NameError: name 'b' is not defined
#     foo()