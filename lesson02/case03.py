# -*- coding:UTF-8 -*-

import random

# 隨機亂數
n = random.randrange(0, 2)
print(n)

n = random.randint(1, 100)
print(n)

# 電腦選號四星彩
n1 = random.randint(0, 9)
n2 = random.randint(0, 9)
n3 = random.randint(0, 9)
n4 = random.randint(0, 9)
print(n1, n2, n3, n4)

#跳脫字元
print("\"")
print("A\n\tB")

print("\""); print("A\n\tB")

a = 100 + \
    200 - 50 * 5 / 10

