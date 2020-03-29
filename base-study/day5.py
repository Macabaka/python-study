# 设计一个函数产生指定长度，验证码由大小写字母和数字构成

# import random

# def generate_code(code_len=4):
#     """
#     生成指定长度的验证码
#     :param code_len:验证码的长度(默认4个字符)
#     ：return:由大小写英文字母和数字构成的随机验证码
#     """
#     all_chars='0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     last_pos = len(all_chars)-1
#     code=""
#     for _ in range(code_len):
#         index = random.randint(0,last_pos)
#         code+=all_chars[index]
#     return code

# #调用函数
# code=generate_code(6)
# print(code)

# 判断一组文件中图片的个数


# def count_image(file_list):
#     """
#     判断一组文件中图片的个数
#     :param file_liat:文件列表
#     :return 图片文件数量
#     """
#     count = 0
#     for file in file_list:
#         if file.endswith('png') or file.endswith('jpg') or file.endswith('webp') or file.endswith('bmp'):
#             count += 1
#     return count


# img_list = ['1.jpg', '2.png', '3.webp', '4.bmp', '5.mp3', '6.wav']
# result = count_image(img_list)
# print('一共有', result, '个图片文件')
