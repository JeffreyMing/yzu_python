s = "she sell sea shell on the sea shore"

print(s)
print("有%d個s" % s.count('s'))
print("有sea這個字嗎? %d" % s.find('sea'))

# 是否都是a-z A-Z =英文字
# 技巧:先利用replace去除空白
print(s.replace(' ', '').isalpha())