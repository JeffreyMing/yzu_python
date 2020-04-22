# 遞迴求解 fibonacci
def f(n):
    print('n = %d'% n)
    if n == 0 or n == 1:
        return n
    return f(n-1) + f(n-2)

print(f(7))