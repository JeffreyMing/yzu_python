
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

# 是否要補牌(True, False)
def draw(pc):
    score = getScore(pc)
    if score >= 9:  # 不補牌
        return False
    if score <= 6:
        return True
    if 6 < score < 8:   #   A、2、3、J、Q、K 剩餘的牌 >= 12 (補)
        count = poker.count(4) + poker.count(5) + poker.count(6) + poker.count(7) + poker.count(8) + poker.count(9) + poker.count(10)
        if count/len(poker) >= 0.5:
            return False
        else:
            pc.append(poker.pop(0))
            return True
    if 8 <= score < 9:
        count = poker.count(3) + poker.count(4) + poker.count(5) + poker.count(6) + poker.count(7) + poker.count(8) + poker.count(9) + poker.count(10)
        if count/len(poker) >= 0.4:
            return False
        else:
            pc.append(poker.pop(0))
            return True

def getWinner(user, pc):
    user_score = getScore(user)
    pc_score = getScore(pc)
    if user_score > 10.5 and pc_score > 10.5:
        return None
    if user_score <= 10.5 and pc_score > 10.5:
        return 'user'
    if user_score > 10.5 and pc_score <= 10.5:
        return 'pc'
    if user_score == pc_score:
        return 'equal'
    if user_score > pc_score:
        return 'user'
    else:
        return 'pc'


# 洗牌
r.shuffle(poker)

#使用者先拿牌
user = []
user.append(poker.pop(0))

while True:
    print('user:', user, getScore(user))
    flag = int(input('是否要補牌? (0:不要,1:要)'))
    if flag ==0:
        break
    user.append(poker.pop(0))

#電腦 拿牌
pc = []
pc.append(poker.pop(0))
while True:
    if draw(pc):
        pc.append(poker.pop(0))
        continue
    break
print('PC: ', pc, getScore(pc))

# 誰贏?
print(getWinner(user, pc))

