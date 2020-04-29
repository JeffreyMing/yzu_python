# 數組 list(可重複) ，Set(不可回復)， Dict(Key-Value)
scores = [100, 90, 80]
scores.append(70)
print(scores)
print(scores[0])  # 取得維度=0的內容
print(len(scores))  # 取得數組長度(有幾筆資料)

for x in scores:
    print(scores.index(x), x)

# 窮舉器
for (i, x) in enumerate(scores):
    print(i, x)
