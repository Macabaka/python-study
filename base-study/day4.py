# 生成斐波那契数列得前20个数
# x=1
# y=1
# z=0
# print(x,',',y,end="")
# for i in range(3,21):
#     z=x+y
#     print(",",z,end="")
#     x=y
#     y=z
# print()


# 找出100以内的完美数
# for num in range(2, 100000):
#     sum = 0
#     for i in range(1, num):
#         if num % i == 0:
#             sum += i
#     if num == sum:
#         print(num)
# print()

# 输出100以内的所有素数
# i = 2
# print('100以内的素数：')
# for num in range(2, 100):
#     for i in range(2, num):
#         if num % i == 0:
#             break
#         else:
#             i = i+1
#     if i >= num:
#         print(num, '', end="")
# print()
