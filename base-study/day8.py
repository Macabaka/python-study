# 列表元素的添加和删除
# list1 = [1, 3, 5, 7, 100]
# list1.append(200)
# list1.insert(1, 400)
# print(list1)
# # 合并两个列表
# list1.extend([1000, 2000])
# print(list1)
# list1 += [100, 200]
# print(list1)
# print(len(list1))
# # 先通过成员运算判断元素是否在列表中，如果存在则删除该元素
# if 100 in list1:
#     list1.remove(100)
# if 1234 in list1:
#     list1.remove(1234)
# print(list1)
# # 从指定的位置删除元素
# list1.pop(0)
# list1.pop(len(list1)-1)
# print(list1)
# # 清空列表元素
# list1.clear()
# print(list1)

# 列表的定义和遍历
# list1 = [1, 3, 5, 7, 100]
# print(list1)
# list2 = ['hello']
# print(list2)
# print(len(list1))
# print(list1[0])
# print(list1[4])
# print(list1[-1])
# print(list1[-3])
# list1[2] = 300
# print(list1)
# # 通过循环用下标进行遍历
# for index in range(len(list1)):
#     print(list1[index])
# # 通过for循环遍历
# for elem in list1:
#     print(elem)
# # 通过enumerate函数处理列表之后再遍历可以同时获得元素
# for index, elem in enumerate(list1):
#     print(index, elem)
