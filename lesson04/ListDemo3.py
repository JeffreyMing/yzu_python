'''
自動補牌機制
電腦若不⾜ 6 (含)點需強迫補牌
電腦若為 9 點（含）以上不需補牌
電腦若為 7、8 點則策略補牌
若為 7 或 7.5 看會爆的機率 > 0.5 (不補)
若為 8 或 8.5 看會爆的機率 > 0.4 (不補)
'''

import random as r

poker = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'] * 4

def getScore(po):
    sum = 0
    for p in po:
        if p == 'A':
            sum = sum + 1
            continue
        if p == 'J' or p == 'Q' or p == 'K':
            sum = sum + 0.5
            continue
        sum += p
    return sum

# 洗牌
r.shuffle(poker)
print(poker)
pc = []
pc.append(poker.pop(0))
# 進入補牌程序
while True:
    score = getScore(pc)
    if score >= 9:  # 不補牌
        break
    if score <= 6:
        pc.append(poker.pop(0))
        continue
    if 6 < score < 8:   #   A、2、3、J、Q、K 剩餘的牌 >= 12 (補)
        count = poker.count(4) + poker.count(5) + poker.count(6) + poker.count(7) + poker.count(8) + poker.count(9) + poker.count(10)
        if count/len(poker) >= 0.5:
            break
        else:
            pc.append(poker.pop(0))
            continue
    if 8 <= score < 9:
        count = poker.count(3) + poker.count(4) + poker.count(5) + poker.count(6) + poker.count(7) + poker.count(8) + poker.count(9) + poker.count(10)
        if count/len(poker) >= 0.4:
            break
        else:
            pc.append(poker.pop(0))
            continue

print(pc)
print(getScore(pc))