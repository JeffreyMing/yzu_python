text = "半徑=10"
# 求圓面積
name, r = text.split('=')
r = int(r)
print("%s 為 %d 的圓面積為 %.2f" % (name, r, r**2 * 3.14))