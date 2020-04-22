# 某數 n 是否是質數

n = int(input("請輸入數字:"))
check = "是質數"
for i in range(2, n//2+1):
    print("%d / %d 餘數= %d" % (n, i, n % i))
    if n % i == 0:
        check = "不是質數"
        break
print(n, check)