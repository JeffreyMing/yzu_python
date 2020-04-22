import random as r

n = r.randint(1, 10)
if n % 2 ==0:
    print('%d 偶數' % n)
else:
    print('%d 奇數' % n)

# 類三元運算子寫法
print('%d %s' % (n, "偶數" if n % 2 == 0 else "奇數"))

# 定義函數，調用函數使用
def isOdd(n):
    return '偶數' if n % 2 == 0 else '奇數'

print('%d %s' % (n, isOdd(n)))