# 杨辉三角

# def main():
#     num = int(input('Number of rows:'))
#     yh = [[]]*num
#     for row in range(len(yh)):
#         yh[row] = [None]* (row+1)
#         for col in range(len(yh[row])):
#             if col ==0 or col==row:
#                 yh[row][col] = 1
#             else:
#                 yh[row][col]=yh[row-1][col]+yh[row-1][col-1]
#             print(yh[row][col],end="\t")
#         print()

# if __name__=='__main__':
#     main()

import os
import time


def main():
    content = "北京欢迎你为你开天辟地"
    while True:
        # 清理屏幕上的输出
        os.system("cls")
        print(content)
        time.sleep(0.2)
        content = content[1:]+content[0]

if __name__ == '__main__':
    main()
